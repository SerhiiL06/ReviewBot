from fastapi import APIRouter, Depends, status
from .service import ReviewService
from typing import Annotated
from .schemes import ReviewScheme


router = APIRouter(prefix="/reviews")


@router.get("/", response_model=list[ReviewScheme])
async def list_of_reviews(service: Annotated[ReviewService, Depends()]):
    return await service.find_reviews()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_review(
    data: ReviewScheme, service: Annotated[ReviewService, Depends()]
):
    return await service.add_review(data.model_dump())
