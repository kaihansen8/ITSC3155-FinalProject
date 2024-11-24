from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class PromoCodeBase(BaseModel):
    promo_code: Optional[str] = None
    rate: Optional[float] = None


class PromoCodeCreate(PromoCodeBase):
    pass


class PromoCodeUpdate(BaseModel):
    promo_code: Optional[str] = None
    rate: Optional[float] = None
    expiration_date: Optional[datetime] = None


class PromoCode(PromoCodeBase):
    id: int
    expiration_date: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True
