from sqlalchemy import Integer, DateTime, Column

from app.db_api.db_session import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())