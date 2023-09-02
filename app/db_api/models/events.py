from sqlalchemy import Column, String, DateTime

from .base_model import BaseModel


class EventModel(BaseModel):
    __tablename__ = "event"

    title = Column(String(128), nullable=False)
    description = Column(String(512), nullable=True)
    date_event = Column(DateTime, nullable=False)
