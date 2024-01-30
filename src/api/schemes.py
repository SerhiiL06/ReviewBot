from pydantic import BaseModel
from typing import Optional


class ReviewScheme(BaseModel):
    user_id: Optional[int] = None
    comment: str
    photo: Optional[str] = None
