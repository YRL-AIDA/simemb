from fastapi import HTTPException
import json
from fastapi import APIRouter
from fastapi import Depends

from src.embedding.schemas import EmbedRequest
from src.embedding.dependencies import get_model_dependency


embedding_router = APIRouter(
    prefix="/embedding"
)


@embedding_router.post("/embed")
async def embed(request: EmbedRequest, model = Depends(get_model_dependency)):
    try:
        # TODO: pydantic validate check
        embeddings = model.process(request.documents)

        return json.dumps({"embeddings": embeddings.tolist()})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
