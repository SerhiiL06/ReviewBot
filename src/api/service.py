from abc import ABC

from pymongo import DESCENDING

from core.mongo import Review


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
