from fastapi import APIRouter
from app.database.mongodb import db

router = APIRouter()

@router.get("/match-outfit/{email}/{color}")

async def match_outfit(
    email: str,
    color: str
):

    outfits = list(

        db.outfits.find({

            "email": email,

            "color": {

                "$regex": color,

                "$options": "i"
            }
        })
    )

    for outfit in outfits:

        outfit["_id"] = str(
            outfit["_id"]
        )

    return outfits