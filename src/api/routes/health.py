from fastapi.routing import APIRouter
import time

router = APIRouter()

START_TIME = time.time()

@router.get("/")
async def health_check():
    """
    Checks if the API is responsive.
    """
    
    return {
        "status": "healthy",
        "uptime_seconds": int(time.time() - START_TIME),
        }
