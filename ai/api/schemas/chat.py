from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Représente les données reçues par l'API.
    """

    message: str


class ClientData(BaseModel):
    """
    Représente les données d'un client transmises au frontend.
    """

    id: int
    nom: str
    email: str
    societe: str
    ville: str


class ArticleData(BaseModel):
    """
    Représente les données d'un article transmises au frontend.
    """

    id: int
    titre: str
    prix: float
    stock: int
    categorie: str
    marque: str


class ChatResponse(BaseModel):
    """
    Représente la réponse envoyée par POST /chat.
    """

    reponse: str
    outil: str | None
    donnees: list[ClientData | ArticleData]