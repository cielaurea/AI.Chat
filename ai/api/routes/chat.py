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


# Routeur dédié aux conversations.
router = APIRouter()


# Création des implémentations utilisées par le workflow.
llm_provider = OllamaProvider()
data_provider = DummyJsonClient()
tool_registry = ToolRegistry()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:

    # Le workflow s'occupe de traiter la demande.
    result = run_chat(
        message=request.message,
        llm_provider=llm_provider,
        data_provider=data_provider,
        tool_registry=tool_registry,
    )

    # Si la demande est hors périmètre, aucune donnée n'est renvoyée.
    if result.tool is None:
        return ChatResponse(
            reponse=result.message,
            outil=None,
            donnees=[],
        )

    # Transforme les clients du domaine en données adaptées à l'API.
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

    # Transforme les articles du domaine en données adaptées à l'API.
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

    else:
        raise ValueError(f"Outil inconnu : {result.tool}")

    # Retourne la réponse au frontend au format prévu par l'API.
    return ChatResponse(
        reponse=result.message,
        outil=result.tool,
        donnees=donnees,
    )