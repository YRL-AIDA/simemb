import json
import os
from typing import Dict, List

import aiofiles

from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel
from contextlib import asynccontextmanager

from src.core.settings import Settings
from src.models.loader import load_text_model, load_vl_model


model = None
settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    print(f"Loading model...")

    if settings.VL:
        model = load_vl_model(settings.VL_MODEL_NAME)
    else:
        model = load_text_model(settings.TEXT_ONLY_MODEL_NAME, settings.DEVICE)

    yield

    del model


app = FastAPI(
    title=f"Qwen3 Text Embeddings Service", 
    version="1.0", 
    lifespan=lifespan
)


class EmbedRequest(BaseModel):
    documents: List[Dict]


@app.post("/embed")
async def embed(request: EmbedRequest):
    try:
        # TODO: pydantic validate check
        embeddings = model.process(request.documents)

        return json.dumps({"embeddings": embeddings.tolist()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    """
    Receives an uploaded image file and saves it locally.
    """
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only images are allowed.")

    file_location = os.path.join(UPLOAD_DIR, file.filename)
    try:
        async with aiofiles.open(file_location, "wb") as buffer:
            while chunk := await file.read(1024):
                await buffer.write(chunk)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"There was an error uploading the file: {e}")
    finally:
        await file.close()

    return {"message": f"Successfully uploaded {file.filename}", "location": file_location}
