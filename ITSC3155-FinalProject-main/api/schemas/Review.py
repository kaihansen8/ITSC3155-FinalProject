from pydantic import BaseModel
from typing import Optional
from .customers import Customer


class ReviewBase(BaseModel):
    review_text: Optional[str] = None
    score: float


class ReviewCreate(ReviewBase):
    customer_id: int


class ReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    score: Optional[float] = None


class Review(ReviewBase):
    id: int
    customer: Optional[Customer] = None

    class ConfigDict:
        from_attributes = True







