from dataclasses import dataclass

from domain.entities import Article, Client


@dataclass
class Response:
    """
    Représente la réponse finale préparée par l'application.

    Elle contient :
    - un texte destiné à l'utilisateur ;
    - le nom de l'outil utilisé, s'il y en a un ;
    - les données récupérées.
    """

    message: str
    tool: str | None
    data: list[Client] | list[Article]


def create_response(
    tool: str | None,
    data: list[Client] | list[Article],
) -> Response:
    """
    Prépare une réponse à partir de l'outil exécuté et de ses données.

    Cette fonction ne récupère aucune donnée et ne contacte aucune API.
    Elle prépare uniquement le résultat qui sera transmis à l'utilisateur.
    """

    # Si aucun outil n'a été sélectionné, la demande est hors périmètre.
    if tool is None:
        return Response(
            message="Désolé, je ne peux répondre qu'aux demandes concernant les clients et les articles.",
            tool=None,
            data=[],
        )

    # Si l'outil utilisé est celui des clients,
    # on prépare un message indiquant combien de clients ont été récupérés.
    if tool == "lister_clients":
        return Response(
            message=f"Voici les {len(data)} premiers clients.",
            tool=tool,
            data=data,
        )

    # Si l'outil utilisé est celui des articles,
    # on prépare un message indiquant combien d'articles ont été récupérés.
    if tool == "lister_articles":
        return Response(
            message=f"Voici les {len(data)} premiers articles.",
            tool=tool,
            data=data,
        )

    # Sécurité supplémentaire : un outil inconnu ne doit pas
    # produire une réponse inattendue.
    raise ValueError(f"Outil inconnu : {tool}")