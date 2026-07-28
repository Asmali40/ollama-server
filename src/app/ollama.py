import requests

from app.constants import (
    OLLAMA_URL,
    DEFAULT_MODEL,
    REQUEST_TIMEOUT
)

def generate(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": DEFAULT_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=REQUEST_TIMEOUT
    )

    response.raise_for_status()

    return response.json()["response"]