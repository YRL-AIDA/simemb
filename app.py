import json
from typing import Dict, List, Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager

from src.core.settings import Settings
from src.models.loader import load_text_model, load_vl_model


model = None
settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    print(f"Loading {settings.MODEL_NAME} model...")

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
    inputs: Union[str, List[str], List[Dict]]


@app.post("/embed")
async def embed(request: EmbedRequest):
    try:
        queries = request.inputs if isinstance(request.inputs, list) else [request.inputs]
        embeddings = model.process(queries)

        return json.dumps({"embeddings": embeddings.tolist()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
