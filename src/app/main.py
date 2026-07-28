from fastapi import 
fromm app.constants import API_TITLE

app = FastAPI(title=API_TITLE)

@app.get("/")
def root():
    return {"status": "running"}