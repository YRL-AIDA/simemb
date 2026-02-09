from src.models.qwen3_embedding import Qwen3Embedder
from src.models.qwen3_vl_embedding import Qwen3VLEmbedder


def load_text_model(model_name: str, device: str) -> Qwen3Embedder:
    return Qwen3Embedder(model_name, device)


def load_vl_model(model_name: str) -> Qwen3VLEmbedder:
    return Qwen3VLEmbedder(model_name)
