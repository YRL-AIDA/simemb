from src.models.qwen3_embedding import Qwen3Embedder


def load_text_model(model_name: str, device: str) -> Qwen3Embedder:
    return Qwen3Embedder(model_name, device)
