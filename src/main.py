from fastapi import FastAPI
from src.api.routes import health

app = FastAPI(title="RecoMicro API", version="v1")

app.include_router(prefix="/health", router=health.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to RecoMicro API"}
