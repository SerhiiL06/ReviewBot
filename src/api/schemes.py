from pydantic import BaseModel


class ReviewScheme(BaseModel):
    user_id: int
    comment: str
    photo: str
