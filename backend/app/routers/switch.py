from fastapi import APIRouter

router = APIRouter()

@router.get("/switch")
async def get_switch_status():
    return {"status": "Online"}
