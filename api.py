from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api/v1/like")
def send_like(uid: str = None):
    if not uid:
        return {"status": "failed", "message": "UID is required"}
    
    # خادم لعبة فري فاير الرسمي المخصص للاتصال والمعاملات اللحظية
    url = "https://freefiremobile.com"
    
    # الرؤوس البرمجية (Headers) لمحاكاة هاتف حقيقي مسجل داخل اللعبة
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Player) AppleWebKit/537.36",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # البيانات المرسلة وتتضمن رقم المعرف الخاص بك (UID)
    data = {
        "target_uid": uid,
        "region": "IND",  # تغيير المنطقة حسب خادم حسابك (مثلاً MEA للشرق الأوسط)
        "source": "lobby"
    }
    
    try:
        # إرسال طلب اللايك المباشر بصيغة POST للسيرفر الرسمي
        response = requests.post(url, json=data, headers=headers, timeout=10)
        
        # إذا قبل السيرفر الطلب وأرسل اللايك بنجاح
        if response.status_code == 200:
            return {"status": "success", "message": f"Likes sent successfully to {uid}"}
        else:
            return {"status": "failed", "message": f"Server rejected request: {response.status_code}"}
    except Exception as e:
        return {"status": "failed", "message": f"Connection error: {str(e)}"}
