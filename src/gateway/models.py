from sqlalchemy import Column, String, DateTime
from src.settings.models import BaseModel


class TokenModel(BaseModel):
    """Модель токена"""
    __tablename__ = "token"

    token = Column(String, nullable=False, index=True, comment="Токен")
    expire = Column(DateTime, nullable=False, comment="Срок действия")
