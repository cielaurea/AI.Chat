from abc import ABC, abstractmethod

from domain.entities import Article, Client


class DataProviderPort(ABC):
    """
    Interface utilisée par l'application pour accéder aux données.

    Le domaine définit ce dont l'application a besoin,
    mais ne sait pas quelle technologie ou quel service
    fournit réellement les données.

    Une implémentation concrète, comme DummyJsonClient,
    devra respecter cette interface.
    """

    @abstractmethod
    def get_clients(self) -> list[Client]:
        """
        Récupère la liste des clients.

        L'implémentation concrète décidera comment les récupérer.
        """
        pass

    @abstractmethod
    def get_articles(self) -> list[Article]:
        """
        Récupère la liste des articles.

        L'implémentation concrète décidera comment les récupérer.
        """
        pass