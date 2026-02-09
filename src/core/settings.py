from pydantic_settings import BaseSettings

import torch

class Settings(BaseSettings):
    TEXT_ONLY_MODEL_NAME: str = "Qwen/Qwen3-Embedding-0.6B"
    VL_MODEL_NAME: str = "Qwen/Qwen3-VL-Embedding-2B"
    MAX_SEQ_LENGTH: int = 8192
    DEVICE: str = "cuda" if torch.cuda.is_available() else "cpu"
    VL: bool = True
    
    class Config:
        env_file = ".env"
