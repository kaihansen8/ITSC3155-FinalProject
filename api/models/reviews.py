from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "ratings_reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review_text = Column(String(500), nullable=True)
    score = Column(Float, nullable=False)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=True)

    sandwich = relationship("Sandwich", back_populates="reviews")








