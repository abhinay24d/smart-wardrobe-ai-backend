from fastapi import APIRouter, HTTPException
from app.database.mongodb import db
from app.models.login_model import UserLogin
from app.utils.security import verify_password
from app.utils.jwt_handler import create_access_token

router = APIRouter()


@router.post("/login")
def login(user: UserLogin):

    existing_user = db.users.find_one({
        "email": user.email
    })

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    password_correct = verify_password(
        user.password,
        existing_user["password"]
    )

    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token(
        data={"email": user.email}
    )

    return {
        "message": "Login Successful",
        "access_token": token
    }