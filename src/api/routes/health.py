from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/")
async def health_check():
    """
    Checks if the API is responsive.
    """
    return {"status": "healthy"}
