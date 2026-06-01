from fastapi import APIRouter, HTTPException

from app.database.mongodb import db
from app.models.register_model import UserRegister

from app.utils.security import hash_password

router = APIRouter()


@router.post("/register")
def register(user: UserRegister):

    existing_user = db.users.find_one({

        "email": user.email
    })

    if existing_user:

        raise HTTPException(

            status_code=400,
            detail="User already exists"
        )

    hashed_password = hash_password(
        user.password
    )

    user_data = {

        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }

    db.users.insert_one(user_data)

    return {

        "message": "User registered successfully"
    }