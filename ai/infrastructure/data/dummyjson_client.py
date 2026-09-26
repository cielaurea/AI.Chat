import httpx

from domain.entities import Article, Client
from domain.ports import DataClientPort


class DummyJsonClient(DataClientPort):
    """
    Communique avec DummyJSON et transforme ses données
    dans les formats utilisés par l'application.
    """

    BASE_URL = "https://dummyjson.com"

    def get_users(self) -> list[dict]:
        """Récupère les 10 premiers utilisateurs."""
        response = httpx.get(
            f"{self.BASE_URL}/users",
            params={"limit": 10},
            timeout=10.0,
        )

        response.raise_for_status()

        # Récupère la liste des utilisateurs dans la réponse JSON.
        return response.json()["users"]

    def get_products(self) -> list[dict]:
        """Récupère les 10 premiers produits."""
        response = httpx.get(
            f"{self.BASE_URL}/products",
            params={"limit": 10},
            timeout=10.0,
        )

        response.raise_for_status()

        # Récupère la liste des produits dans la réponse JSON.
        return response.json()["products"]

    def get_clients(self) -> list[Client]:
        """Transforme les utilisateurs en entités Client."""
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
        """Transforme les produits en entités Article."""
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