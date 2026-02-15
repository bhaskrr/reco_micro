from fastapi import FastAPI

app = FastAPI(title="RecoMicro API", version="v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to RecoMicro API"}
