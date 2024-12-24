from pydantic import BaseModel

class CreateDocumentResponse(BaseModel):
    document_id: str
    document_base64: str
    message: str