from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.ocr_service import OCRService

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
ocr_service = OCRService()

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/upload", response_class=HTMLResponse)
async def upload_image(request: Request, file: UploadFile = File(...)):
    file_location = f"app/static/images/{file.filename}"
    OCRService.save_uploaded_file(await file.read(), file_location)
    extracted_text = OCRService.perform_ocr(file_location)
    image_path = image_path = f"images/{file.filename}"
    return templates.TemplateResponse("result.html", {"request": request, "text": extracted_text, "image_path": image_path})
