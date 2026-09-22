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


class LlmProviderPort(ABC):
    """
    Interface utilisée par l'application pour communiquer avec
    un modèle de langage.

    Le domaine définit uniquement ce dont l'application a besoin :
    envoyer une question au modèle et recevoir sa réponse.

    Il ne connaît pas Ollama, HTTP, une clé API ou un modèle particulier.

    L'implémentation concrète sera placée dans infrastructure/providers/.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Envoie un prompt au modèle et retourne sa réponse sous forme de texte.

        L'application utilise cette méthode sans connaître
        la technologie utilisée derrière.
        """
        pass