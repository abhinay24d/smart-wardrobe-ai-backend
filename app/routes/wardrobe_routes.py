from fastapi import APIRouter, UploadFile, File, Form, Depends
from app.utils.auth_middleware import verify_user
from app.database.mongodb import db
import shutil
import os

router = APIRouter()


UPLOAD_FOLDER = "uploads"


@router.post("/upload-wardrobe")
def upload_wardrobe(
    category: str = Form(...),
    color: str = Form(...),
    season: str = Form(...),
    occasion: str = Form(...),
    image: UploadFile = File(...),
    user=Depends(verify_user)
):

    # Create uploads folder if not exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Save image path
    image_path = f"{UPLOAD_FOLDER}/{image.filename}"

    # Save image locally
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Save data in MongoDB
    wardrobe_item = {
        "email": user["email"],
        "category": category,
        "color": color,
        "season": season,
        "occasion": occasion,
        "image_path": image_path
    }

    db.wardrobe.insert_one(wardrobe_item)

    return {
        "message": "Wardrobe Item Uploaded Successfully"
    }