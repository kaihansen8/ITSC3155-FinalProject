from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from pydantic import EmailStr

class PaymentInformation(Base):
    __tablename__ = 'payment_information'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer_name = Column(String(100))
    #customer_email = Column(String(100), nullable=True)
    customer_email = Column(EmailStr, nullable=True)
    customer_phone_number = Column(String(10), nullable=True)
    customer_address = Column(String(300), nullable=True)

    customers = relationship("Customers", backref="payment_information")