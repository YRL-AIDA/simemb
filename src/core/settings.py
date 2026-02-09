from pydantic_settings import BaseSettings

import torch

class Settings(BaseSettings):
    MODEL_NAME: str = "Qwen/Qwen3-Embedding-0.6B"
    MAX_SEQ_LENGTH: int = 8192
    DEVICE: str = "cuda" if torch.cuda.is_available() else "cpu"
    
    class Config:
        env_file = ".env"
