from dataclasses import dataclass

from domain.ports import LlmProviderPort, ToolRegistryPort
from domain.tools import ToolName


@dataclass
class Plan:
    tool: ToolName | None


def create_plan(
    message: str,
    llm_provider: LlmProviderPort,
    tool_registry: ToolRegistryPort,
) -> Plan:
    """
    Demande au modèle quel outil utiliser pour la question.
    """

    # Récupère les outils disponibles
    tools = tool_registry.get_tools()

    # Prépare la description des outils pour le modèle
    tools_description = "\n".join(
        f"- {tool.name.value} : {tool.description}"
        for tool in tools
    )
    # Prompt pour le modéle 
    prompt = f"""
Tu es le module de décision d'un assistant.

Ton rôle est uniquement de déterminer quel outil utiliser
pour répondre à la question de l'utilisateur.

Outils disponibles :
{tools_description}

Règles :
- Si la question demande la liste des clients, réponds exactement : lister_clients
- Si la question demande la liste des articles ou des produits, réponds exactement : lister_articles
- Pour toute autre question, réponds exactement : aucun

Tu dois répondre avec une seule valeur parmi :
lister_clients
lister_articles
aucun

Question de l'utilisateur :
{message}
""".strip()

    # Demande au modèle de prendre une décision sur l'outil à utiliser
    model_response = llm_provider.generate(prompt).strip().lower()

    # Si le modéle choisi  l'outil clients 
    if model_response == ToolName.LISTER_CLIENTS.value:
        return Plan(tool=ToolName.LISTER_CLIENTS)

    # Si le modéle choisi  l'outil articles
    if model_response == ToolName.LISTER_ARTICLES.value:
        return Plan(tool=ToolName.LISTER_ARTICLES)

    # Toute autre réponse est considérée comme hors périmètre
    return Plan(tool=None)