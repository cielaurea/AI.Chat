from application.execute import ToolExecutor
from application.nodes.plan import create_plan
from application.respond import Response, create_response
from domain.ports import DataProviderPort, LlmProviderPort, ToolRegistryPort


def run_chat(
    message: str,
    llm_provider: LlmProviderPort,
    data_provider: DataProviderPort,
    tool_registry: ToolRegistryPort,
) -> Response:
    """
    Exécute le parcours complet d'une demande utilisateur.

    Le workflow suit trois étapes :
    1. décider quel outil utiliser ;
    2. exécuter l'outil sélectionné ;
    3. préparer la réponse finale.

    Les dépendances techniques sont reçues depuis l'extérieur.
    La couche application ne crée donc aucune implémentation
    provenant de l'infrastructure.
    """

    # ToolExecutor utilise le port DataProviderPort.
    # Il ne connaît pas l'API DummyJSON concrète.
    executor = ToolExecutor(data_provider)

    # Première étape : analyser la demande et déterminer
    # quel outil doit éventuellement être utilisé.
    #
    # Le modèle et le catalogue sont également reçus via leurs ports.
    plan = create_plan(
        message=message,
        llm_provider=llm_provider,
        tool_registry=tool_registry,
    )

    # Si aucune demande autorisée n'a été détectée,
    # on prépare directement une réponse hors périmètre.
    if plan.tool is None:
        return create_response(
            tool=None,
            data=[],
        )

    # Deuxième étape : exécuter l'outil choisi par le plan.
    # Les données proviennent donc du fournisseur de données
    # réellement injecté dans l'application.
    data = executor.execute(plan.tool)

    # Troisième étape : transformer les données réellement reçues
    # en réponse structurée destinée à l'utilisateur.
    return create_response(
        tool=plan.tool.value,
        data=data,
    )