import structlog
from pathlib import Path
from pypdf import PdfReader
import uuid
from app.models.document import Document

logger = structlog.get_logger()

class DocumentParsingService:
    def __init__(self):
        pass

    async def extract_text(self, document: Document) -> str:
        """
        Extract text from the specified document based on its format.
        """
        logger.info("extracting_text", document_id=document.id, file_path=document.file_path)
        
        file_path = Path(document.file_path)
        if not file_path.exists():
            logger.error("file_not_found", file_path=str(file_path))
            raise FileNotFoundError(f"File not found: {file_path}")

        extracted_text = ""
        
        try:
            if document.format == "pdf":
                extracted_text = self._parse_pdf(file_path)
            elif document.format in ["txt", "md"]:
                extracted_text = self._parse_text(file_path)
            else:
                raise ValueError(f"Unsupported format: {document.format}")
                
            logger.info("text_extracted_successfully", length=len(extracted_text))
            return extracted_text
            
        except Exception as e:
            logger.error("text_extraction_failed", error=str(e))
            raise

    def _parse_pdf(self, file_path: Path) -> str:
        reader = PdfReader(str(file_path))
        text_parts = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)
        return "\n\n".join(text_parts)

    def _parse_text(self, file_path: Path) -> str:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
