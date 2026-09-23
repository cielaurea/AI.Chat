from fastapi import APIRouter

from api.schemas.chat import (
    ArticleData,
    ChatRequest,
    ChatResponse,
    ClientData,
)
from application.graph import run_chat
from infrastructure.data.dummyjson_client import DummyJsonClient
from infrastructure.providers.ollama_provider import OllamaProvider
from infrastructure.tools.registry import ToolRegistry


# Crée un routeur FastAPI dédié aux routes de conversation.
# Le routeur sera ensuite enregistré dans api/main.py.
router = APIRouter()


# Les implémentations concrètes sont créées ici, à la frontière de l'application.
#
# La couche application ne connaît que les ports :
# LlmProviderPort, DataClientPort et ToolRegistryPort.
#
# C'est donc l'API qui assemble les différentes implémentations
# nécessaires au fonctionnement réel du service.
llm_provider = OllamaProvider()
data_provider = DummyJsonClient()
tool_registry = ToolRegistry()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """
    Reçoit une question de l'utilisateur et retourne la réponse de l'assistant.

    Le parcours complet est réalisé par la couche application :
    1. le modèle décide quel outil utiliser ;
    2. l'outil récupère les données ;
    3. l'application prépare la réponse finale.

    Cette route se charge uniquement de faire le lien
    entre HTTP et la couche application.
    """

    # On transmet le message reçu à notre workflow applicatif.
    # Les implémentations concrètes sont injectées via leurs ports.
    result = run_chat(
        message=request.message,
        llm_provider=llm_provider,
        data_provider=data_provider,
        tool_registry=tool_registry,
    )

    # Une demande hors périmètre produit une réponse sans données.
    if result.tool is None:
        return ChatResponse(
            reponse=result.message,
            outil=None,
            donnees=[],
        )

    # Si l'outil utilisé concerne les clients,
    # on transforme les entités Client en modèles de réponse API.
    if result.tool == "lister_clients":
        donnees = [
            ClientData(
                id=client.id,
                nom=client.nom,
                email=client.email,
                societe=client.societe,
                ville=client.ville,
            )
            for client in result.data
        ]

    # Si l'outil utilisé concerne les articles,
    # on transforme les entités Article en modèles de réponse API.
    elif result.tool == "lister_articles":
        donnees = [
            ArticleData(
                id=article.id,
                titre=article.titre,
                prix=article.prix,
                stock=article.stock,
                categorie=article.categorie,
                marque=article.marque,
            )
            for article in result.data
        ]

    # Cette situation ne devrait normalement jamais arriver,
    # car le workflow n'autorise que les outils définis dans le domaine.
    else:
        raise ValueError(f"Outil inconnu : {result.tool}")

    # FastAPI transformera automatiquement ce modèle Pydantic
    # en JSON correspondant exactement au contrat de l'API.
    return ChatResponse(
        reponse=result.message,
        outil=result.tool,
        donnees=donnees,
    )