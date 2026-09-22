import httpx

from core.config import settings
from domain.ports import LlmProviderPort


class OllamaProvider(LlmProviderPort):
    """
    Implémentation concrète du port LlmProviderPort avec Ollama Cloud.

    Cette classe appartient à l'infrastructure car elle connaît
    les détails techniques nécessaires pour communiquer avec Ollama :
    URL, clé API, modèle et format de la requête HTTP.

    La couche application n'utilisera pas directement cette classe.
    Elle utilisera uniquement LlmProviderPort.
    """

    def generate(self, prompt: str) -> str:
        """
        Envoie un prompt à Ollama Cloud et retourne la réponse du modèle.

        Le prompt est fourni par la couche application.
        Cette classe se charge uniquement de la communication technique
        avec l'API Ollama.
        """

        # L'URL, la clé API et le modèle sont récupérés depuis la configuration.
        # Ces informations ne sont donc pas écrites directement dans le code.
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
            },
            timeout=60.0,
        )

        # Si Ollama retourne une erreur HTTP, elle est propagée
        # plutôt que de produire une réponse incorrecte.
        response.raise_for_status()

        # L'API Ollama retourne la réponse du modèle
        # dans message.content.
        return response.json()["message"]["content"]