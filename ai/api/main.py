from fastapi import FastAPI

from api.routes.chat import router as chat_router


# Point d'entrée HTTP du service : crée l'application FastAPI.
app = FastAPI(title="AI.Chat")


# Ajoute les routes liées au chat à l'application.
app.include_router(chat_router)


@app.get("/health")
def health():
    """
    Vérifie que le service FastAPI est disponible.
    """
    return {"status": "ok"}