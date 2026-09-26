from application.nodes.plan import create_plan
from domain.ports import LlmProviderPort, ToolRegistryPort
from domain.tools import ToolDefinition, ToolName


class FakeLlmProvider(LlmProviderPort):
    """Faux fournisseur de modèle utilisé pour les tests."""

    def __init__(self, response: str):
        self.response = response

    def generate(self, prompt: str) -> str:
        return self.response


class FakeToolRegistry(ToolRegistryPort):
    """Faux registre d'outils utilisé pour les tests."""

    def get_tools(self) -> list[ToolDefinition]:
        return [
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


def test_create_plan_for_clients():
    llm_provider = FakeLlmProvider(ToolName.LISTER_CLIENTS.value)
    tool_registry = FakeToolRegistry()

    plan = create_plan(
        "Donne-moi la liste des clients",
        llm_provider,
        tool_registry,
    )

    assert plan.tool == ToolName.LISTER_CLIENTS


def test_create_plan_for_articles():
    llm_provider = FakeLlmProvider(ToolName.LISTER_ARTICLES.value)
    tool_registry = FakeToolRegistry()

    plan = create_plan(
        "Donne-moi la liste des articles",
        llm_provider,
        tool_registry,
    )

    assert plan.tool == ToolName.LISTER_ARTICLES


def test_create_plan_for_out_of_scope_question():
    llm_provider = FakeLlmProvider("aucun")
    tool_registry = FakeToolRegistry()

    plan = create_plan(
        "Quel temps fait-il aujourd'hui ?",
        llm_provider,
        tool_registry,
    )

    assert plan.tool is None