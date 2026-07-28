from fastapi import FastAPI

from app.constants import API_TITLE
from app.router.chat import router as chat_router

app = FastAPI(title=API_TITLE)
app.include_router(chat_router)

@app.get("/")
def root():
    return {"status": "running"}