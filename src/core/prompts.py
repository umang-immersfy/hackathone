from typing import Dict
import jinja2
from src.preset import preamble
from src.api import exception_handler
from src.schemas.request import CreateDocumentRequest

PromptDict = Dict[str, str]

@exception_handler
def prepare_prompt_for_technology(request: CreateDocumentRequest) -> PromptDict:
    user_script = jinja2.Template(preamble.user_script).render(
        {
            "name": request.name,
            "abstract": request.abstract,
            "requirements": "\n".join(request.requirements),
        }
    )
    return {"system": preamble.technology_prompt, "user": user_script}
