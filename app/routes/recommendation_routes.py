from fastapi import APIRouter
from app.database.mongodb import db

router = APIRouter()


@router.get("/recommend/{email}/{occasion}/{season}")
def recommend_outfit(

    email: str,
    occasion: str,
    season: str
):

    outfits = list(

        db.outfits.find({

    "email": email,
    "occasion": {"$regex": occasion, "$options": "i"},
    "season": {"$regex": season, "$options": "i"}

}, {"_id": 0})
    )

    if len(outfits) == 0:

        return {

            "message": "No matching outfits found"
        }

    return {

        "message": "Recommended outfits",

        "recommendations": outfits
    }