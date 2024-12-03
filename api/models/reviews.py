from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "ratings_reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # Optional message the customer can leave (500 char count limit)
    review_text = Column(String(500), nullable=True)
    # Overall score the customer can leave
    score = Column(Float, nullable=False)
    # Customer's ID from the customer table
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    # Relationship between the customer and the review
    customer = relationship("Customers", back_populates="review")








