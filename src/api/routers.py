from typing import Annotated

from fastapi import APIRouter, Depends, Query, status

from src.utils.regex import local_regex, methods_regex

from .schemes import ReviewScheme
from .service import ReviewService

router = APIRouter(prefix="/reviews")


@router.get("/", response_model=list[ReviewScheme])
async def list_of_reviews(
    service: Annotated[ReviewService, Depends()],
    method: str = Query(None, regex=methods_regex),
    location: str = Query(None, regex=local_regex),
):
    return service.find_reviews(method, location)
