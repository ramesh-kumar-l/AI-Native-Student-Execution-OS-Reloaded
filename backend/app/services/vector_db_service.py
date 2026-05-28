import structlog
import chromadb
from chromadb.config import Settings
import uuid

logger = structlog.get_logger()

class VectorDBService:
    def __init__(self, persist_directory: str = "./chroma_db"):
        self.persist_directory = persist_directory
        # Use persistent client for production readiness
        self.client = chromadb.PersistentClient(path=self.persist_directory)
        self.collection_name = "student_knowledge_base"
        
        # Get or create the main collection
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"}
        )
        logger.info("vector_db_initialized", collection=self.collection_name)

    async def upsert_document_chunks(self, document_id: uuid.UUID, user_id: uuid.UUID, chunks: list[str]):
        """
        Embeds and stores text chunks associated with a specific document and user.
        """
        logger.info("upserting_chunks", document_id=document_id, chunk_count=len(chunks))
        
        ids = [f"{document_id}_{i}" for i in range(len(chunks))]
        metadatas = [{"document_id": str(document_id), "user_id": str(user_id)} for _ in chunks]
        
        self.collection.add(
            documents=chunks,
            metadatas=metadatas,
            ids=ids
        )

    async def semantic_search(self, query: str, user_id: uuid.UUID, n_results: int = 5) -> list[str]:
        """
        Retrieves the most relevant chunks for a given query, filtered by user.
        """
        logger.info("semantic_search", query=query, user_id=user_id)
        
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where={"user_id": str(user_id)}
        )
        
        if results and "documents" in results and results["documents"]:
            return results["documents"][0]
        return []
