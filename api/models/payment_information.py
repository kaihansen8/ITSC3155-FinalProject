from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class PaymentInformation(Base):
    __tablename__ = 'payment_information'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer_card = Column(String(16), nullable=False)
    promo_code = Column(String(16), nullable=True)

    customers = relationship("Customers", backref="payment_information")