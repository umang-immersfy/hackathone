from fastapi import APIRouter, Depends
from src.model import groq_wrapper
from src.schemas.request import CreateDocumentRequest
from src.schemas.response import CreateDocumentResponse
from src.api.endpoints import GroqModel
from src.core import prompts
from src.api import exception_handler, LOGGER

users_router = APIRouter()

@users_router.post("/create_documents", response_model=CreateDocumentResponse)
@exception_handler
def create_documents(request: CreateDocumentRequest) -> CreateDocumentResponse:
    LOGGER.info("Received request to create documents")
    prompt_dict = prompts.prepare_prompt_for_technology(request)
    LOGGER.debug(f"Prepared prompt dictionary: {prompt_dict}")
    
    GroqModel.generate_response(prompt_dict)
    LOGGER.info("Generated response from GroqModel")
    
    doc_id = "101"
    document_base64 = "base64"
    LOGGER.info(f"Document created with ID: {doc_id}")
    
    return CreateDocumentResponse(
        document_id=doc_id,
        document_base64=document_base64,
        message="Documents created successfully!"
    )
