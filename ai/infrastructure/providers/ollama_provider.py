import httpx

from core.config import settings
from domain.ports import LlmProviderPort


class OllamaProvider(LlmProviderPort):
    """
    Implémentation concrète du port LlmProviderPort avec Ollama Cloud.

    Cette classe appartient à l'infrastructure car elle connaît
    les détails techniques nécessaires pour communiquer avec Ollama :
    URL, clé API, modèle et format de la requête HTTP.

    La couche application n'utilise pas directement cette classe.
    Elle utilise uniquement LlmProviderPort.
    """

    def generate(self, prompt: str) -> str:
        """
        Envoie un prompt à Ollama Cloud et retourne la réponse du modèle.

        Le modèle doit uniquement choisir une valeur parmi les outils
        disponibles ou "aucun". La génération est donc volontairement
        limitée afin d'éviter qu'il produise une réponse longue.
        """

        # L'URL, la clé API et le modèle proviennent de la configuration.
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
                    # Le modèle doit prendre une décision déterministe.
                    "temperature": 0,
                    # Les réponses attendues sont extrêmement courtes.
                    "num_predict": 5,
                },
            },
            timeout=60.0,
        )

        # Si Ollama retourne une erreur HTTP, elle est propagée
        # plutôt que de produire une réponse incorrecte.
        response.raise_for_status()

        # L'API Ollama retourne la réponse du modèle
        # dans message.content.
        return response.json()["message"]["content"]