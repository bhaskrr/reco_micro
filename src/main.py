from fastapi import FastAPI
from src.api.routes import health

from src.db.database import Base, engine
import src.db.models

app = FastAPI(title="RecoMicro API", version="v1")

Base.metadata.create_all(engine)

app.include_router(prefix="/health", router=health.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to RecoMicro API"}
