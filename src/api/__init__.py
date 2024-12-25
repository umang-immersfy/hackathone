from functools import wraps
from fastapi import HTTPException
from src.core import logger as custom_logger

def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            raise HTTPException(
                status_code=500,
                detail="An error occurred while processing the request."
            )
    return wrapper


LOGGER = custom_logger.initialize_logger("ai-server")
