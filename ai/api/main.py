from fastapi import FastAPI

from api.routes.chat import router as chat_router


# Création de l'application FastAPI.
# Cette application constitue le point d'entrée HTTP de notre service IA.
app = FastAPI(title="AI.Chat")


# Enregistre les routes de conversation dans l'application.
# Le endpoint métier POST /chat devient ainsi accessible par FastAPI.
app.include_router(chat_router)


@app.get("/health")
def health():
    """
    Vérifie que le service FastAPI fonctionne correctement.

    Cette route est indépendante du workflow de conversation
    et permet notamment de vérifier la disponibilité du service.
    """

    # Réponse simple utilisée comme indicateur de santé du service.
    return {"status": "ok"}