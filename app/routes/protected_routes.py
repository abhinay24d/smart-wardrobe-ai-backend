from fastapi import APIRouter, Depends
from app.utils.auth_middleware import verify_user

router = APIRouter()


@router.get("/profile")
def profile(user=Depends(verify_user)):

    return {
        "message": "Protected Route Accessed",
        "user": user
    }