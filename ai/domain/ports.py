from abc import ABC, abstractmethod

from domain.entities import Article, Client
from domain.tools import ToolDefinition


class DataClientPort(ABC):
    """
    Définit les méthodes nécessaires pour accéder aux données
    """

    @abstractmethod
    def get_clients(self) -> list[Client]:
        """
        Récupère la liste des clients
        """
        pass

    @abstractmethod
    def get_articles(self) -> list[Article]:
        """
        Récupère la liste des articles
        """
        pass


class LlmProviderPort(ABC):
    """
    Définit la méthode utilisée pour communiquer avec le modèle
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Envoie un prompt au modèle et retourne sa réponse
        """
        pass


class ToolRegistryPort(ABC):

    @abstractmethod
    def get_tools(self) -> list[ToolDefinition]:
        """
        Retourne la liste des outils disponibles
        """
        pass