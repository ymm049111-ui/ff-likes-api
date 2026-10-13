from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api/v1/like")
def send_like(uid: str = None):
    if not uid:
        return {"status": "failed", "message": "UID is required"}
    
    # الرابط الجديد المباشر والمعدل لإرسال المتغيرات
    url = f"https://railway.app"
    params = {"uid": uid}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        return response.json()
    except:
        return {"status": "failed", "message": "API Server Error"}
