from PIL import Image
import pytesseract

class OCRService:
    @staticmethod
    def perform_ocr(file_location: str) -> str:
        img = Image.open(file_location)
        text = pytesseract.image_to_string(img)
        return text

    @staticmethod
    def save_uploaded_file(file: bytes, file_location: str):
        import os
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        with open(file_location, "wb") as image:
            image.write(file)
