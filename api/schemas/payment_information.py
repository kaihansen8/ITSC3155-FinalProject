from typing import Optional
from pydantic import BaseModel



class PaymentInformationBase(BaseModel):
    customer_id: int
    customer_card: str
    promo_code: str


class PaymentInformationCreate(PaymentInformationBase):
    pass


class PaymentInformationUpdate(BaseModel):
    customer_card: Optional[str] = None
    promo_code: Optional[str] = None
    


class PaymentInformation(PaymentInformationBase):
    id: int

    class ConfigDict:
        from_attributes = True
