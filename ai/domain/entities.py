from dataclasses import dataclass


@dataclass
class Client:
    """
    Représente un client dans notre domaine métier.

    Cette entité ne dépend pas de DummyJSON :
    elle contient uniquement les informations dont notre application a besoin.
    """

    id: int
    nom: str
    email: str
    societe: str
    ville: str


@dataclass
class Article:
    """
    Représente un article dans notre domaine métier.

    La structure est volontairement indépendante
    de la structure utilisée par l'API DummyJSON.
    """

    id: int
    titre: str
    prix: float
    stock: int
    categorie: str
    marque: str