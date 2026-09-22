from dataclasses import dataclass
from enum import Enum


class ToolName(str, Enum):
    """
    Noms des outils que l'assistant est autorisé à utiliser.

    Le modèle pourra choisir uniquement l'un de ces outils
    ou aucun outil si la demande est hors périmètre.
    """

    LISTER_CLIENTS = "lister_clients"
    LISTER_ARTICLES = "lister_articles"


@dataclass(frozen=True)
class ToolDefinition:
    """
    Décrit un outil disponible dans le catalogue.

    Le catalogue fournit au modèle les informations nécessaires
    pour comprendre ce que fait chaque outil.
    """

    name: ToolName
    description: str
    parameters: dict[str, object]


# Catalogue officiel des outils disponibles pour l'assistant.
# Il sera utilisé lors de l'étape « Décider » pour présenter
# les possibilités au modèle.
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