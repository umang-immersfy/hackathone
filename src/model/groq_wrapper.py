import abc
from src.core import parameters
import openai
from groq import Groq
from src.api import exception_handler


class GroqModelWrapper(abc.ABC):
    def __init__(self):
        self.client = Groq(
            api_key=parameters.GROQ_API_KEY,
        )

    @exception_handler
    def prepare_input(self, prompt_dict):
        conversation = []
        for role, content in prompt_dict.items():
            conversation.append(
                {
                    "role": role,
                    "content": content,
                }
            )
        return conversation

    @exception_handler
    def generate_response(self, prompt_dict):
        conversation = self.prepare_input(prompt_dict)
        if conversation is None:
            raise ValueError("Error preparing input")
        chat_completion = self.client.chat.completions.create(
            messages=conversation,
            model="llama3-8b-8192",
            response_format={"type": "json_object"}
        )
        print(chat_completion.choices[0].message.content)
