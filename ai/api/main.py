from fastapi import FastAPI

app = FastAPI(title="AI.Chat")

@app.get("/health")
def health():
    return {"status": "ok"}