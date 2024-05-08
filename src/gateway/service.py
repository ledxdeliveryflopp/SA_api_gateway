from dataclasses import dataclass
from datetime import datetime
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.requests import Request
from src.gateway.repository import TokenRepository
from src.settings.depends import get_session
from src.settings.exceptions import BadToken


@dataclass
class TokenService(TokenRepository):
    """Сервис для работы с токенами"""

    async def verify_token(self, request: Request) -> status or dict:
        """Проверка токена из заголовка"""
        header_token = request.headers.get("Authorization")
        if not header_token:
            raise BadToken
        header_token = header_token.replace("Bearer ", "")
        token = await self.find_token(header_token)
        if not token:
            raise BadToken
        if token.expire < datetime.utcnow():
            await self.session_delete_object(token)
            raise BadToken
        return status.HTTP_200_OK


async def init_token_service(session: AsyncSession = Depends(get_session)) -> TokenService:
    """Инициализация сервиса токенов"""
    service = TokenService(session)
    return service
