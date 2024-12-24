from functools import wraps
from fastapi import HTTPException

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
