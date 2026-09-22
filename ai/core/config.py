import os

from dotenv import load_dotenv


# Charge les variables présentes dans le fichier .env
# afin qu'elles soient disponibles via os.getenv().
load_dotenv()


class Settings:
    """
    Contient la configuration utilisée par l'application.

    Les informations sensibles, comme la clé API Ollama,
    ne sont pas écrites directement dans le code.
    Elles sont récupérées depuis les variables d'environnement.
    """

    # URL de base utilisée pour communiquer avec Ollama.
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "")

    # Clé API utilisée pour authentifier les requêtes vers Ollama.
    OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "")

    # Nom du modèle utilisé par l'application.
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma4")


# Instance de configuration utilisée par le reste de l'application.
settings = Settings()