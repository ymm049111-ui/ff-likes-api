from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api/v1/like")
def send_like(uid: str):
    url = f"https://railway.app{uid}"
    try:
        response = requests.get(url, timeout=10)
        return response.json()
    except:
        return {"status": "failed", "message": "Error"}
      
