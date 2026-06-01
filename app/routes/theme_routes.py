from fastapi import APIRouter
from app.database.mongodb import db

router = APIRouter()

@router.get("/home-theme/{season}")

async def get_theme(season: str):

    theme = db.themes.find_one({

        "season": season
    })

    if theme:

        theme["_id"] = str(theme["_id"])

    return theme