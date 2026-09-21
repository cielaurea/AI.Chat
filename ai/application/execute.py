from domain.entities import Article, Client
from domain.ports import DataProviderPort
from domain.tools import ToolName


class ToolExecutor:
    """
    Exécute les outils disponibles dans notre application.

    Cette classe appartient à la couche application.
    Elle ne connaît pas DummyJSON ni la manière dont les données
    sont réellement récupérées.

    Elle utilise uniquement le port DataProviderPort défini dans le domaine.
    """

    def __init__(self, data_provider: DataProviderPort):
        """
        Initialise l'exécuteur avec un fournisseur de données.

        Le fournisseur est reçu de l'extérieur afin que cette classe
        ne soit pas directement liée à une implémentation particulière.
        """
        self.data_provider = data_provider

    def execute(self, tool_name: ToolName) -> list[Client] | list[Article]:
        """
        Exécute l'outil demandé et retourne les données correspondantes.

        Le nom de l'outil est défini par le domaine grâce à ToolName.
        """

        # Si l'outil demandé correspond aux clients,
        # on utilise la méthode métier prévue pour récupérer les clients.
        if tool_name == ToolName.LISTER_CLIENTS:
            return self.data_provider.get_clients()

        # Si l'outil demandé correspond aux articles,
        # on utilise la méthode métier prévue pour récupérer les articles.
        if tool_name == ToolName.LISTER_ARTICLES:
            return self.data_provider.get_articles()

        # Cette situation ne devrait normalement pas arriver,
        # car seuls les outils définis dans ToolName sont autorisés.
        raise ValueError(f"Outil inconnu : {tool_name}")