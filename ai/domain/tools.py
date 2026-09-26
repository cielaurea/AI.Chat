from dataclasses import dataclass
from enum import Enum


class ToolName(str, Enum):
    """
    Définit les outils disponibles pour l'assistant
    """

    LISTER_CLIENTS = "lister_clients"
    LISTER_ARTICLES = "lister_articles"


@dataclass(frozen=True)
class ToolDefinition:
    """
    Décrit un outil disponible dans le catalogue
    """

    name: ToolName
    description: str
    parameters: dict[str, object]


# Catalogue des outils disponibles pour l'assistant
TOOL_CATALOG = [
    ToolDefinition(
        name=ToolName.LISTER_CLIENTS,
        description="Liste les 10 premiers clients.",
        parameters={},
    ),
    ToolDefinition(
        name=ToolName.LISTER_ARTICLES,
        description="Liste les 10 premiers articles.",
        parameters={},
    ),
]