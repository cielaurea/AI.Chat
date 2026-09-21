from dataclasses import dataclass

from domain.tools import ToolName


@dataclass
class Plan:
    """
    Représente le résultat de l'étape de planification.

    Le plan indique simplement quel outil doit être utilisé.
    Si aucune demande autorisée n'est détectée, tool vaut None.
    """

    tool: ToolName | None


def create_plan(message: str) -> Plan:
    """
    Analyse le message de l'utilisateur et détermine l'outil à utiliser.

    Pour notre test, l'assistant ne doit gérer que deux demandes :
    - lister les clients ;
    - lister les articles.

    Toute autre demande reste hors périmètre.
    """

    # On met le message en minuscules et on retire les espaces inutiles
    # afin de faciliter les comparaisons.
    normalized_message = message.strip().lower()

    # Si le message parle des clients, on sélectionne l'outil correspondant.
    if "client" in normalized_message:
        return Plan(tool=ToolName.LISTER_CLIENTS)

    # Si le message parle des articles, on sélectionne l'outil correspondant.
    if "article" in normalized_message:
        return Plan(tool=ToolName.LISTER_ARTICLES)

    # Si aucune demande connue n'est détectée,
    # aucun outil ne doit être exécuté.
    return Plan(tool=None)