import abc
from src.core import parameters
import openai
from groq import Groq


class GroqModelWrapper(abc.ABC):
    def __init__(self):
        try:
            self.client = Groq(
                api_key=parameters.GROQ_API_KEY,
            )
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Groq client: {e}")

    def prepare_input(self, prompt_dict):
        conversation = []
        try:
            for role, content in prompt_dict.items():
                conversation.append(
                    {
                        "role": role,
                        "content": content,
                    }
                )
            return conversation
        except Exception as e:
            return f"Error preparing input: {e}"

    def generate_response(self, prompt_dict):
        try:
            conversation = self.prepare_input(prompt_dict)
            if isinstance(conversation, str) and conversation.startswith("Error"):
                raise ValueError(conversation)
            chat_completion = self.client.chat.completions.create(
                messages=conversation,
                model="llama3-8b-8192",
                response_format={"type": "json_object"}
            )
            print(chat_completion.choices[0].message.content)
        except Exception as e:
            print(f"Error generating response: {e}")
