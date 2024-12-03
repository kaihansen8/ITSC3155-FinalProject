from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from .order_details import OrderDetail



class PaymentInformationBase(BaseModel):
    customer_id: int
    customer_name: str


class PaymentInformationCreate(PaymentInformationBase):
    pass


class PaymentInformationUpdate(BaseModel):
    customer_name: Optional[str] = None
    


class PaymentInformation(PaymentInformationBase):
    id: int
    customer_email: Optional[EmailStr] = None
    customer_phone_number: Optional[str] = None
    customer_address: Optional[str] = None

    class ConfigDict:
        from_attributes = True
