from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from manga_ocr import MangaOcr
from PIL import Image
import io
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Japanese OCR API", version="1.0.0")

mocr = None

@app.on_event("startup")
async def startup_event():
    global mocr
    logger.info("Loading MangaOCR model...")
    mocr = MangaOcr()
    logger.info("MangaOCR model loaded successfully!")

@app.get("/")
async def root():
    return {"message": "Japanese OCR API is running"}

@app.post("/ocr")
async def extract_text(file: UploadFile = File(...)):
    """
    Extract Japanese text from an uploaded image using MangaOCR.
    
    Args:
        file: Image file (PNG, JPG, JPEG, etc.)
    
    Returns:
        JSON response with extracted text
    """
    if not mocr:
        raise HTTPException(status_code=503, detail="OCR model not initialized")
    
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        text = mocr(image)
        
        return JSONResponse(
            content={
                "status": "success",
                "text": text,
                "filename": file.filename
            }
        )
    
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)