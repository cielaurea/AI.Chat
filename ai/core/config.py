import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    """Regroupe la configuration utilisée par l'application."""

    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "")
    OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma4")


settings = Settings()