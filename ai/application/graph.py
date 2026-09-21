from application.nodes.plan import create_plan
from application.respond import Response, create_response
from application.execute import ToolExecutor
from infrastructure.data.dummyjson_client import DummyJsonClient


def run_chat(message: str) -> Response:
    """
    Exécute le parcours complet d'une demande utilisateur.

    Le workflow suit trois étapes :
    1. planifier la demande ;
    2. exécuter l'outil sélectionné ;
    3. préparer la réponse finale.

    Cette fonction représente le point d'entrée de la logique
    applicative avant son exposition par l'API FastAPI.
    """

    # On crée le fournisseur de données concret.
    # Il sera utilisé par ToolExecutor pour récupérer les données.
    data_provider = DummyJsonClient()

    # ToolExecutor utilise le port du domaine,
    # sans avoir besoin de connaître les détails de l'API externe.
    executor = ToolExecutor(data_provider)

    # Première étape : analyser la demande et déterminer
    # quel outil doit éventuellement être utilisé.
    plan = create_plan(message)

    # Si aucune demande autorisée n'a été détectée,
    # on prépare directement une réponse hors périmètre.
    if plan.tool is None:
        return create_response(
            tool=None,
            data=[],
        )

    # Deuxième étape : exécuter l'outil choisi par le plan.
    data = executor.execute(plan.tool)

    # Troisième étape : transformer le résultat de l'exécution
    # en réponse structurée destinée à l'utilisateur.
    return create_response(
        tool=plan.tool.value,
        data=data,
    )