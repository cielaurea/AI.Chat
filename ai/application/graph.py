from application.execute import ToolExecutor
from application.nodes.plan import create_plan
from application.respond import Response, create_response
from domain.ports import DataClientPort, LlmProviderPort, ToolRegistryPort


def run_chat(
    message: str,
    llm_provider: LlmProviderPort,
    data_provider: DataClientPort,
    tool_registry: ToolRegistryPort,
) -> Response:
    

    # Prépare l'exécution des outils avec le fournisseur de données.
    executor = ToolExecutor(data_provider)

    # Détermine quel outil utiliser pour la demande.
    plan = create_plan(
        message=message,
        llm_provider=llm_provider,
        tool_registry=tool_registry,
    )

    if plan.tool is None:
        return create_response(
            tool=None,
            data=[],
        )

    # Exécute l'outil choisi et récupère les données.
    data = executor.execute(plan.tool)

    # Prépare la réponse finale
    return create_response(
        tool=plan.tool.value,
        data=data,
    )