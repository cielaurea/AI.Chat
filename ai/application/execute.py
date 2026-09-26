from domain.entities import Article, Client
from domain.ports import DataClientPort
from domain.tools import ToolName


class ToolExecutor:
    """
    Exécute l'outil choisi pour récupérer les données.
    """

    def __init__(self, data_provider: DataClientPort):
        """
        Initialise l'exécuteur avec le fournisseur de données.
        """
        self.data_provider = data_provider

    def execute(self, tool_name: ToolName) -> list[Client] | list[Article]:
        """
        Exécute l'outil demandé et retourne les données correspondantes.
        """

        # Récupère les clients si l'outil choisi est lister_clients.
        if tool_name == ToolName.LISTER_CLIENTS:
            return self.data_provider.get_clients()

        # Récupère les articles si l'outil choisi est lister_articles.
        if tool_name == ToolName.LISTER_ARTICLES:
            return self.data_provider.get_articles()

        # Un outil non prévu indique un problème dans le workflow.
        raise ValueError(f"Outil inconnu : {tool_name}")