from fastapi import APIRouter, UploadFile, File, Form
from app.database.mongodb import db

import shutil
import os
import uuid

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# UPLOAD OUTFIT
@router.post("/upload-outfit")
async def upload_outfit(

    email: str = Form(...),
    category: str = Form(...),
    color: str = Form(...),
    season: str = Form(...),
    occasion: str = Form(...),

    image: UploadFile = File(...)
):

    try:

        print("\n========== UPLOAD REQUEST ==========")

        print("EMAIL:", email)
        print("CATEGORY:", category)
        print("COLOR:", color)
        print("SEASON:", season)
        print("OCCASION:", occasion)
        print("IMAGE:", image.filename)

        # Create unique filename
        extension = image.filename.split(".")[-1]

        unique_filename = f"{uuid.uuid4()}.{extension}"

        file_path = os.path.join(
            UPLOAD_FOLDER,
            unique_filename
        )

        # Save image
        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                image.file,
                buffer
            )

        # Save to MongoDB
        outfit_data = {

            "email": email,
            "category": category,
            "color": color,
            "season": season,
            "occasion": occasion,
            "image_path": file_path,
        }

        result = db.outfits.insert_one(
            outfit_data
        )

        print("UPLOAD SUCCESS")
        print("OUTFIT ID:", result.inserted_id)

        return {

            "success": True,

            "message":
                "Outfit uploaded successfully",

            "outfit_id":
                str(result.inserted_id),

            "data": {

                "email": email,
                "category": category,
                "color": color,
                "season": season,
                "occasion": occasion,
                "image_path": file_path
            }
        }

    except Exception as e:

        print("\nUPLOAD ERROR")
        print(str(e))

        return {

            "success": False,
            "error": str(e)
        }


# GET ALL OUTFITS
@router.get("/get-outfits/{email}")
def get_outfits(email: str):

    try:

        outfits = list(

            db.outfits.find(

                {"email": email},

                {"_id": 0}
            )
        )

        return outfits

    except Exception as e:

        print("GET OUTFITS ERROR")
        print(str(e))

        return {
            "error": str(e)
        }