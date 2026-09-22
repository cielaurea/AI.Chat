from dataclasses import dataclass

from domain.ports import LlmProviderPort, ToolRegistryPort
from domain.tools import ToolName


@dataclass
class Plan:
    """
    Représente le résultat de l'étape de planification.

    Le plan indique quel outil doit être utilisé.
    Si le modèle considère que la demande est hors périmètre,
    tool vaut None.
    """

    tool: ToolName | None


def create_plan(
    message: str,
    llm_provider: LlmProviderPort,
    tool_registry: ToolRegistryPort,
) -> Plan:
    """
    Demande au modèle de déterminer l'outil correspondant à la question.

    Le modèle reçoit :
    - la question de l'utilisateur ;
    - le catalogue des outils disponibles.

    Le catalogue est obtenu via ToolRegistryPort.
    L'application ne dépend donc pas directement
    de l'implémentation concrète du registre.

    Cette fonction appartient à la couche application.
    Elle ne connaît pas Ollama ni la manière dont le catalogue
    est réellement stocké.
    """

    # On récupère le catalogue via le port défini dans le domaine.
    # L'application ne connaît pas directement ToolRegistry.
    tools = tool_registry.get_tools()

    # On transforme les définitions d'outils en texte
    # pour les présenter au modèle dans le prompt.
    tools_description = "\n".join(
        f"- {tool.name.value} : {tool.description}"
        for tool in tools
    )

    # Le prompt donne au modèle une règle très stricte :
    # il ne peut choisir qu'un outil du catalogue ou "aucun".
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

    # L'application utilise uniquement le port LlmProviderPort.
    # Elle ne sait pas si le modèle est fourni par Ollama ou par une autre technologie.
    model_response = llm_provider.generate(prompt).strip().lower()

    # Le modèle a choisi l'outil permettant de récupérer les clients.
    if model_response == ToolName.LISTER_CLIENTS.value:
        return Plan(tool=ToolName.LISTER_CLIENTS)

    # Le modèle a choisi l'outil permettant de récupérer les articles.
    if model_response == ToolName.LISTER_ARTICLES.value:
        return Plan(tool=ToolName.LISTER_ARTICLES)

    # Toute autre réponse du modèle est considérée comme hors périmètre.
    # Cela évite qu'une réponse inattendue entraîne l'exécution
    # d'un outil qui n'a pas été explicitement autorisé.
    return Plan(tool=None)