import httpx

from core.config import settings
from domain.ports import LlmProviderPort


class OllamaProvider(LlmProviderPort):
    """
    Communique avec Ollama pour obtenir une réponse du modèle
    """

    def generate(self, prompt: str) -> str:
        """
        Envoie le prompt à Ollama et retourne la réponse du modèle
        """

        response = httpx.post(
            f"{settings.OLLAMA_BASE_URL}/api/chat",
            headers={
                "Authorization": f"Bearer {settings.OLLAMA_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": settings.OLLAMA_MODEL,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                "stream": False,
                "options": {
                    "temperature": 0,
                    "num_predict": 5,
                },
            },
            timeout=60.0,
        )

        response.raise_for_status()

        return response.json()["message"]["content"]