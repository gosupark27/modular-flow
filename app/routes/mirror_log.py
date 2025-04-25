from fastapi import APIRouter, Request 
from datetime import datetime 

router = APIRouter()

@router.post("/")
async def log_mirror_entry(request: Request): 
    data = await request.json()

    log_entry = {
        "user_id": data.get("user_id"), 
        "name": data.get("name"),
        "selected_option": data.get("prompt_text"), 
        "prompt_text": data.get("prompt_text"), 
        "timestamp": datetime.utcnow().isoformat(), 
        "flame_role_inference": data.get("flame_role_inference") 
    }

    print("📥 New Mirror Log Entry:", log_entry)

    # TODO: Push to Notion or Firebase 

    return {"status": "logged", "data": log_entry}
