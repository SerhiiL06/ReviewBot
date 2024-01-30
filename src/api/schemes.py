from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class ReviewScheme(BaseModel):
    model_config = ConfigDict(
        str_to_lower=True, json_encoders={datetime: datetime.date}
    )

    user_id: Optional[int] = None
    location: str
    comment: str
    method: str
    create_date: datetime
    photo: Optional[str] = None
