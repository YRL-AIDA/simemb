import torch

from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    # Service
    service_address: str = "0.0.0.0"
    service_port: int = 8000

    # ML
    text_only_model_name: str = "Qwen/Qwen3-Embedding-0.6B"
    vl_model_name: str = "Qwen/Qwen3-VL-Embedding-2B"
    max_seq_length: int = 8192
    use_vl: bool = True
    device: str = "cuda" if torch.cuda.is_available() else "cpu"

    # Files
    upload_dir: str = "uploads"
    upload_url: str = "upload/upload-image"

    # JSON
    encoding: str = "utf-8"

    class Config:
        env_file = ".env"



settings = Settings()
print(settings.model_dump())
