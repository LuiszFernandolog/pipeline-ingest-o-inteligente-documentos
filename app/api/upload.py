from fastapi import APIRouter, UploadFile, File

from app.services.upload_service import save_upload_file

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = await save_upload_file(file)

    return {
        "filename": file.filename,
        "saved_at": file_path
    }