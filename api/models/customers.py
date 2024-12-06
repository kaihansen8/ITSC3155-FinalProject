from sqlalchemy import Column, Integer, String
from ..dependencies.database import Base

class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(12), nullable=False)
    address = Column(String(300), nullable=False)