from pydantic import BaseModel
from typing import Optional


class ReviewBase(BaseModel):
    review_text: Optional[str] = None
    score: float
    sandwich_id: int


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    score: Optional[float] = None
    sandwich_id: Optional[int] = None


class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True





