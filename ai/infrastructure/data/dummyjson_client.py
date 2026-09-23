import httpx

from domain.entities import Article, Client
from domain.ports import DataClientPort


class DummyJsonClient(DataClientPort):
    """
    Implémentation du port DataClientPort avec l'API DummyJSON.

    Cette classe appartient à l'infrastructure :
    elle connaît donc le détail de communication avec l'API externe.
    """

    # URL de base de l'API externe utilisée pour récupérer les données.
    BASE_URL = "https://dummyjson.com"

    def get_users(self) -> list[dict]:
        """Récupère les 10 premiers utilisateurs depuis DummyJSON."""
        response = httpx.get(
            f"{self.BASE_URL}/users",
            params={"limit": 10},
            timeout=10.0,
        )

        # Déclenche une erreur si l'API retourne un code HTTP d'erreur.
        response.raise_for_status()

        # DummyJSON renvoie les utilisateurs dans la clé "users".
        return response.json()["users"]

    def get_products(self) -> list[dict]:
        """Récupère les 10 premiers articles depuis DummyJSON."""
        response = httpx.get(
            f"{self.BASE_URL}/products",
            params={"limit": 10},
            timeout=10.0,
        )

        # Déclenche une erreur si l'API retourne un code HTTP d'erreur.
        response.raise_for_status()

        # DummyJSON renvoie les articles dans la clé "products".
        return response.json()["products"]

    def get_clients(self) -> list[Client]:
        """
        Transforme les utilisateurs de DummyJSON en entités Client.

        DummyJSON utilise plusieurs objets imbriqués.
        Ici, on les transforme dans le format utilisé par notre domaine.
        """
        users = self.get_users()

        return [
            Client(
                id=user["id"],
                nom=f"{user['firstName']} {user['lastName']}",
                email=user["email"],
                societe=user["company"]["name"],
                ville=user["address"]["city"],
            )
            for user in users
        ]

    def get_articles(self) -> list[Article]:
        """
        Transforme les produits de DummyJSON en entités Article.

        Cette méthode masque complètement la structure de DummyJSON
        au reste de l'application.
        """
        products = self.get_products()

        return [
            Article(
                id=product["id"],
                titre=product["title"],
                prix=product["price"],
                stock=product["stock"],
                categorie=product["category"],
                marque=product["brand"],
            )
            for product in products
        ]