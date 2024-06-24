from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import ocr

app = FastAPI()

app.include_router(ocr.router, tags=["OCR"])
app.mount("/static", StaticFiles(directory="app/static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
