from fastapi import FastAPI
from src.api.router import all_routers


app = FastAPI()

for router in all_routers:
    app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
