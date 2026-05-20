from fastapi import APIRouter, UploadFile, File

from app.services.upload_service import save_upload_file
from app.services.pdf_service import extract_text_from_pdf
from app.services.ai_service import analyze_document

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = await save_upload_file(file)

    extracted_text = extract_text_from_pdf(file_path)

    ai_result = analyze_document(extracted_text)

    return {
        "filename": file.filename,
        "saved_at": file_path,
        "text_preview": extracted_text[:500],
        "ai_analysis": ai_result
    }