from sqlalchemy import BigInteger, String, Column, DateTime

from .base_model import BaseModel


class UserModel(BaseModel):
    __tablename__ = "user"

    tg_id = Column(BigInteger, nullable=False, index=True, unique=True)
    first_name = Column(String(length=64), nullable=True)
    last_name = Column(String(length=64), nullable=True)
    username = Column(String(length=64), nullable=True, unique=True)
    joined_date = Column(DateTime)
