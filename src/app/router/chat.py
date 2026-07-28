from fastapi import FastAPI
from app.schema import ChatRequest, ChatResponse
from app.ollama import generate

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    answer = generate(request.prompt)

    return ChatResponse(
        answer = answer
    )