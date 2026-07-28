from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def main(): 
    return {"status": "backend läuft"}

@app.post("/chat")
def chat(request: ChatRequest):
    ollama_response = requests.post("http://localhost:11434/api/generate", 
    json={
        "model": "qwen2.5:1.5b",
        "prompt": request.prompt,
        "stream": False
    })
    data = ollama_response.json()
    return {"answer": data["response"]}