from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepo:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
    
    @abstractmethod
    async def create(self, *args, **kwargs):
        ...

    @abstractmethod
    async def get_one(self, *args, **kwargs):
        ...
    
    @abstractmethod
    async def get_many(self, *args, **kwargs):
        ...
    
    @abstractmethod
    async def update(self, *args, **kwargs):
        ...
    
    @abstractmethod
    async def delete(self, *args, **kwargs):
        ...
    
