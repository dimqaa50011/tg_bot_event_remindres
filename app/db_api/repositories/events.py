from typing import Union, Optional
from datetime import datetime

from loguru import logger
from sqlalchemy import select

from ..models.events import EventModel
from .base_repo import BaseRepo


class EventRepo(BaseRepo):
    async def create(self, title: str, date_event: datetime, description: Optional[str] = None) -> Union[EventModel, None]:
        new_event = EventModel(
            title=title,
            description=description,
            date_event=date_event,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        try:
            self._session.add(new_event)
            await self._session.commit()
            return new_event
        except Exception as ex:
            logger.warning(ex)
            return None

    async def get_one(self, _id: int) -> Union[EventModel, None]:
        stmt = select(EventModel).where(EventModel.id == _id)
        result = await self._session.scalar(stmt)
        return result

    async def get_many(self, *args, **kwargs):
        return await super().get_many(*args, **kwargs)

    async def update(self, *args, **kwargs):
        return await super().update(*args, **kwargs)

    async def delete(self, *args, **kwargs):
        return await super().delete(*args, **kwargs)
