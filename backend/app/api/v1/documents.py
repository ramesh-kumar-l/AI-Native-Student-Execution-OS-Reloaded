import uuid
import os
import shutil
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.api.dependencies import get_db, get_current_user
from app.models.user import User
from app.models.document import Document
from app.api.schemas.knowledge import DocumentResponse
from app.services.document_parsing_service import DocumentParsingService
from app.services.vector_db_service import VectorDBService
from app.services.knowledge_extraction_service import KnowledgeExtractionService

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

parsing_service = DocumentParsingService()
vector_db = VectorDBService()
extraction_service = KnowledgeExtractionService()

async def process_document_background(document_id: uuid.UUID, db: AsyncSession):
    # In a real app, this runs in ARQ/Celery. For now, simulating async background task.
    # Note: DB session handling in raw background tasks can be tricky; simplified here.
    result = await db.execute(select(Document).where(Document.id == document_id))
    doc = result.scalars().first()
    if not doc:
        return
        
    try:
        doc.status = "processing"
        await db.commit()
        
        # 1. Parse text
        text = await parsing_service.extract_text(doc)
        
        # 2. Chunk text (simple chunking for demo)
        chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
        
        # 3. Vector DB sync
        await vector_db.upsert_document_chunks(doc.id, doc.user_id, chunks)
        
        # 4. Generate Flashcards
        flashcards = await extraction_service.generate_flashcards(text, doc)
        if flashcards:
            db.add_all(flashcards)
            
        doc.status = "indexed"
        await db.commit()
        
    except Exception as e:
        doc.status = "failed"
        doc.error_message = str(e)
        await db.commit()

@router.post("/upload", response_model=DocumentResponse)
async def upload_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Save file locally
    file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{file.filename}")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # Create DB record
    format_type = file.filename.split('.')[-1].lower() if '.' in file.filename else "txt"
    doc = Document(
        user_id=current_user.id,
        title=file.filename,
        file_path=file_path,
        format=format_type
    )
    db.add(doc)
    await db.commit()
    await db.refresh(doc)
    
    # Trigger processing
    background_tasks.add_task(process_document_background, doc.id, db)
    
    return doc

@router.get("/", response_model=List[DocumentResponse])
async def get_documents(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Document).where(Document.user_id == current_user.id))
    return list(result.scalars().all())
