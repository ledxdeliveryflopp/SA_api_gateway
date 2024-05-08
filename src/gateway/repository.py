from dataclasses import dataclass
from sqlalchemy import Select
from src.gateway.models import TokenModel
from src.settings.service import BaseService


@dataclass
class TokenRepository(BaseService):
    """Репозиторий для работы с Токенами"""

    async def find_token(self, token: str) -> TokenModel:
        token = await self.session.execute(Select(TokenModel).where(TokenModel.token == token))
        return token.scalar()
