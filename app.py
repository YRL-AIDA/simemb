import json
from typing import List, Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager

from src.core.settings import Settings
from src.models.loader import load_text_model


model = None
settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    print(f"Loading {settings.MODEL_NAME} model...")

    model = load_text_model(settings.MODEL_NAME, settings.DEVICE)

    yield

    del model


app = FastAPI(
    title=f"Qwen3 Text Embeddings Service", 
    version="1.0", 
    lifespan=lifespan
)


class EmbedRequest(BaseModel):
    inputs: Union[str, List[str]]


@app.post("/embed")
async def embed(request: EmbedRequest):
    try:
        queries = request.inputs if isinstance(request.inputs, list) else [request.inputs]
        embeddings = model.embed(queries)

        return json.dumps({"embeddings": embeddings.tolist()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
