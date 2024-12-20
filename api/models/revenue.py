from sqlalchemy import Column, Integer, DECIMAL, DATETIME
from ..dependencies.database import Base


class Revenue(Base):
    __tablename__ = "revenue"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    money = Column(DECIMAL(4,2), index=True, nullable=False, server_default='0.0')
    date = Column(DATETIME, index=True, nullable=False, server_default='1970-01-01')