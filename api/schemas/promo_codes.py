from datetime import datetime
from typing import Optional
from pydantic import BaseModel



class PromoCodeBase(BaseModel):
    promo_code: Optional[str] = None
    rate: Optional[float] = None
    expiration_date: Optional[datetime] = None


class PromoCodeCreate(PromoCodeBase):
    pass


class PromoCodeUpdate(BaseModel):
    promo_code: Optional[str] = None
    rate: Optional[float] = None
    expiration_date: Optional[datetime] = None


class PromoCode(PromoCodeBase):
    id: int

    class ConfigDict:
        from_attributes = True
