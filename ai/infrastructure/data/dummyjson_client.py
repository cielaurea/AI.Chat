import httpx


class DummyJsonClient:
    BASE_URL = "https://dummyjson.com"

    def get_users(self) -> list[dict]:
        response = httpx.get(
            f"{self.BASE_URL}/users",
            params={"limit": 10},
            timeout=10.0,
        )
        response.raise_for_status()
        return response.json()["users"]

    def get_products(self) -> list[dict]:
        response = httpx.get(
            f"{self.BASE_URL}/products",
            params={"limit": 10},
            timeout=10.0,
        )
        response.raise_for_status()
        return response.json()["products"]