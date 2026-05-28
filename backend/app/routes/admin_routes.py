from fastapi import APIRouter
router = APIRouter()
@router.get("/stats")
async def get_stats():
    return {"total_users": 0, "active_sessions": 0}
