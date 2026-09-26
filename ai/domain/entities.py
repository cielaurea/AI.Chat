from dataclasses import dataclass


@dataclass
class Client:
    """
    Représente un client utilisé par l'application.
    """

    id: int
    nom: str
    email: str
    societe: str
    ville: str


@dataclass
class Article:
    """
    Représente un article utilisé par l'application.
    """

    id: int
    titre: str
    prix: float
    stock: int
    categorie: str
    marque: str