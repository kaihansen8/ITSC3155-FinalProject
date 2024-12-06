from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME
from ..dependencies.database import Base

class PromoCode(Base):
    __tablename__ = 'promo_codes'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(15), nullable=True)
    rate = Column(DECIMAL(10,2), nullable=False, default=0)
    expiration_date = Column(DATETIME, nullable=True)