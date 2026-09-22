from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Représente les données reçues par l'API lorsqu'un utilisateur
    envoie une question à l'assistant.

    Exemple :
    {
        "message": "donne-moi la liste des clients"
    }
    """

    # Question envoyée par l'utilisateur.
    message: str


class ClientData(BaseModel):
    """
    Représente les données nettoyées d'un client
    que l'API transmet au frontend.
    """

    # Identifiant du client.
    id: int

    # Nom et prénom du client.
    nom: str

    # Adresse e-mail du client.
    email: str

    # Nom de la société du client.
    societe: str

    # Ville du client.
    ville: str


class ArticleData(BaseModel):
    """
    Représente les données nettoyées d'un article
    que l'API transmet au frontend.
    """

    # Identifiant de l'article.
    id: int

    # Titre de l'article.
    titre: str

    # Prix de l'article.
    prix: float

    # Quantité disponible en stock.
    stock: int

    # Catégorie de l'article.
    categorie: str

    # Marque de l'article.
    marque: str


class ChatResponse(BaseModel):
    """
    Représente la réponse complète envoyée par POST /chat.

    Elle respecte le contrat demandé dans le sujet :
    - reponse : texte destiné à l'utilisateur ;
    - outil : outil utilisé, ou None si la demande est hors périmètre ;
    - donnees : données nettoyées récupérées par l'outil.
    """

    # Réponse textuelle affichée à l'utilisateur.
    reponse: str

    # Nom de l'outil utilisé, ou None si aucun outil n'a été utilisé.
    outil: str | None

    # Données nettoyées retournées par l'outil.
    # La liste peut contenir des clients, des articles ou être vide.
    donnees: list[ClientData | ArticleData]