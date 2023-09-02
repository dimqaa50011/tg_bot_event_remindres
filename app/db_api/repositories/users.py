from typing import Union, Optional
from datetime import datetime

from loguru import logger
from sqlalchemy.exc import IntegrityError

from ..models.users import UserModel
from .base_repo import BaseRepo


class UserRepo(BaseRepo):
    async def create(
            self, 
            tg_id: int, first_name: Optional[str] = None,
            last_name: Optional[str] = None, 
            username: Optional[str] = None
    ) -> Union[UserModel, None]:
        new_user = UserModel(
            tg_id=tg_id,
            first_name=first_name, last_name=last_name,
            username=username,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        try:
            self._session.add(new_user)
            await self._session.commit()
            return new_user
        except IntegrityError as ex:
            logger.warning(ex)
            return None

    async def get_one(self, *args, **kwargs):
        return await super().get_many(*args, **kwargs)

    async def get_many(self, *args, **kwargs):
        return await super().get_many(*args, **kwargs)

    async def update(self, *args, **kwargs):
        return await super().update(*args, **kwargs)

    async def delete(self, *args, **kwargs):
        return await super().delete(*args, **kwargs)
