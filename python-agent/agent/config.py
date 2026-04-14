import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    """Application configuration loaded from environment variables."""

    model: str = os.getenv("OLLAMA_MODEL", "gpt-oss:120b-cloud")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")


settings = Settings()
