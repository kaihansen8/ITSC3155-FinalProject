from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class RevenueBase(BaseModel):
    money: float
    date: datetime


class RevenueCreate(RevenueBase):
    pass


class RevenueUpdate(BaseModel):
    money: Optional[float] = None
    date: Optional[datetime] = None


class Revenue(RevenueBase):
    id: int

    class ConfigDict:
        from_attributes = True