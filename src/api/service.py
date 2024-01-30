from abc import ABC
from core.mongo import Review
from pymongo import DESCENDING


class AbstractReview(ABC):
    def find_reviews(self, location: str = None):
        raise NotImplemented()


class ReviewService(AbstractReview):
    def find_reviews(self, method: str = None, location: str = None) -> list[Review]:
        filter_data = {}
        if method:
            filter_data.update({"method": method})
        if location:
            filter_data.update({"location": location})
        result = Review.find(filter_data).sort([("create_date", DESCENDING)])
        return result
