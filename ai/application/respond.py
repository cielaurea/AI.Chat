from dataclasses import dataclass

from domain.entities import Article, Client


@dataclass
class Response:
    """
    Contient la réponse finale préparée par l'application.
    """

    message: str
    tool: str | None
    data: list[Client] | list[Article]


def create_response(
    tool: str | None,
    data: list[Client] | list[Article],
) -> Response:
    """
    Prépare la réponse finale à partir de l'outil utilisé et des données.
    """

    # Si aucun outil n'a été sélectionné, la demande est hors périmètre
    if tool is None:
        return Response(
            message="Désolé, je ne peux répondre qu'aux demandes concernant les clients et les articles.",
            tool=None,
            data=[],
        )

    # Prépare la réponse pour les clients
    if tool == "lister_clients":
        return Response(
            message=f"Voici les {len(data)} premiers clients.",
            tool=tool,
            data=data,
        )

    # Prépare la réponse pour les articles
    if tool == "lister_articles":
        return Response(
            message=f"Voici les {len(data)} premiers articles.",
            tool=tool,
            data=data,
        )

    # Un outil inconnu indique un problème dans le workflow
    raise ValueError(f"Outil inconnu : {tool}")