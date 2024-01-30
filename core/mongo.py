import os

from pymongo.mongo_client import MongoClient

user = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASSWORD")
name = os.getenv("MONGO_NAME")


class MongoTools:
    _DB_URL = f"mongodb+srv://{user}:{password}@{name}.hpdseom.mongodb.net/?retryWrites=true&w=majority"

    @classmethod
    def get_client(cls) -> MongoClient:
        return MongoClient(cls._DB_URL)

    @property
    def get_review_model(self):
        client = self.get_client()
        db = client.reviews

        model = db["reviews"]

        return model


Review = MongoTools().get_review_model
