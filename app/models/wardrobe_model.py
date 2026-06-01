from pydantic import BaseModel


class WardrobeItem(BaseModel):

    category: str
    color: str
    season: str
    occasion: str