from application.nodes.plan import create_plan
from domain.ports import LlmProviderPort, ToolRegistryPort
from domain.tools import ToolDefinition, ToolName


class FakeLlmProvider(LlmProviderPort):
    """
    Faux fournisseur de modèle utilisé uniquement pour les tests.

    Il évite d'appeler Ollama réellement.
    La réponse du modèle est contrôlée directement par le test.
    """

    def __init__(self, response: str):
        # Stocke la réponse que le faux modèle devra retourner.
        self.response = response

    def generate(self, prompt: str) -> str:
        # Retourne la réponse prédéfinie sans appeler un vrai modèle.
        return self.response


class FakeToolRegistry(ToolRegistryPort):
    """
    Faux registre d'outils utilisé uniquement pour les tests.

    Il fournit les deux outils autorisés par l'application,
    avec la même structure que le catalogue réel.
    """

    def get_tools(self) -> list[ToolDefinition]:
        # Le test fournit les mêmes informations minimales
        # que le catalogue réel pour les deux outils.
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
    """
    Vérifie qu'une réponse du modèle indiquant
    'lister_clients' produit bien le bon outil dans le plan.
    """

    # On simule ici la décision du modèle pour une question
    # concernant les clients.
    llm_provider = FakeLlmProvider(ToolName.LISTER_CLIENTS.value)

    # On utilise un faux registre pour fournir le catalogue des outils.
    tool_registry = FakeToolRegistry()

    # On demande à la fonction de planifier une question
    # concernant les clients.
    plan = create_plan(
        "Donne-moi la liste des clients",
        llm_provider,
        tool_registry,
    )

    # Le résultat attendu est l'outil de récupération des clients.
    assert plan.tool == ToolName.LISTER_CLIENTS


def test_create_plan_for_articles():
    """
    Vérifie qu'une réponse du modèle indiquant
    'lister_articles' produit bien le bon outil dans le plan.
    """

    # On simule la décision du modèle pour une question
    # concernant les articles.
    llm_provider = FakeLlmProvider(ToolName.LISTER_ARTICLES.value)

    # On utilise le même faux catalogue d'outils.
    tool_registry = FakeToolRegistry()

    # On demande à la fonction de planifier une question
    # concernant les articles.
    plan = create_plan(
        "Donne-moi la liste des articles",
        llm_provider,
        tool_registry,
    )

    # Le résultat attendu est l'outil de récupération des articles.
    assert plan.tool == ToolName.LISTER_ARTICLES


def test_create_plan_for_out_of_scope_question():
    """
    Vérifie qu'une question hors périmètre
    ne sélectionne aucun outil.
    """

    # On simule la réponse "aucun" que le modèle doit donner
    # lorsqu'une question ne concerne ni les clients ni les articles.
    llm_provider = FakeLlmProvider("aucun")

    # On utilise le même faux catalogue que pour les autres tests.
    tool_registry = FakeToolRegistry()

    # On demande à la fonction de planifier une question
    # qui ne fait pas partie du périmètre de l'application.
    plan = create_plan(
        "Quel temps fait-il aujourd'hui ?",
        llm_provider,
        tool_registry,
    )

    # Aucune donnée ne doit être récupérée pour cette question.
    assert plan.tool is None