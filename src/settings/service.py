from dataclasses import dataclass
from src.settings.repository import BaseRepository


@dataclass
class BaseService(BaseRepository):
    """Базовый сервис для работы с Бд"""

    async def save_object(self, saved_object: object):
        """Сохранение объекта в БД"""
        return await self.session_save_object(saved_object)

    async def delete_object(self, deleted_object: object):
        """Удаление объекта из БД"""
        return await self.session_delete_object(deleted_object)
