from abc import ABC
from core.mongo import Review
from datetime import datetime


class AbstractReview(ABC):
    def add_review(self, comment: str, photo: str):
        raise NotImplemented()

    def find_reviews(self, location=None):
        raise NotImplemented()


class ReviewService(AbstractReview):
    def add_review(self, data: dict) -> dict:
        result = Review.insert_one(
            {
                "user_id": data.get("user_id"),
                "comment": data.get("comment"),
                "photo": data.get("photo"),
            }
        )
        return {"message": "CREATE", "code": "201", "objectId": str(result.inserted_id)}

    def find_reviews(self, location: str = None) -> list[Review]:
        return Review.find()
