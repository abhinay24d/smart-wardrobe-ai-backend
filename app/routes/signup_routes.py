from fastapi import APIRouter
from app.models.user_model import UserSignup
from app.database.mongodb import db
from app.utils.security import hash_password

router = APIRouter()


@router.post("/signup")
def signup(user: UserSignup):

    existing_user = db.users.find_one(
        {"email": user.email}
    )

    if existing_user:
        return {
            "message": "User already exists"
        }

    user_dict = user.dict()

    user_dict["password"] = hash_password(
        user.password
    )

    db.users.insert_one(user_dict)

    return {
        "message": "User Created Successfully"
    }