from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Pipeline API online"}


app.include_router(upload_router)