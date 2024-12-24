from pydantic import BaseModel
from typing import List

class CreateDocumentRequest(BaseModel):
    name: str
    abstract: str
    requirements: List[str]