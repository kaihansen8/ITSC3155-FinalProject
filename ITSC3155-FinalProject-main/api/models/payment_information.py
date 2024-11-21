from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class PaymentInformation(Base):
    __tablename__ = 'payment_information'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), ForeignKey('orders.customer_name'))
    customer_email = Column(String(100), nullable=True)
    customer_phone_number = Column(String(10), nullable=True)
    customer_address = Column(String(300), nullable=True)

    orders = relationship('Order', backref='payment_information')