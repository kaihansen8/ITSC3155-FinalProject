from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from .order_details import OrderDetail



class PaymentInformationBase(BaseModel):
    customer_id: int
    customer_card: str
    promo_code: str


class PaymentInformationCreate(PaymentInformationBase):
    pass


class PaymentInformationUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_card: Optional[str] = None
    promo_code: Optional[str] = None
    


class PaymentInformation(PaymentInformationBase):

    class ConfigDict:
        from_attributes = True
