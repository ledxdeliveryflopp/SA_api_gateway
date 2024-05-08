from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Настройки БД"""
    user: str
    postgres_password: str
    host: str
    port: str
    database_name: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def full_database_url(self) -> str:
        return (f"postgresql+asyncpg://{self.user}:{self.postgres_password}@{self.host}:"
                f"{self.port}/{self.database_name}")

class Settings(BaseSettings):
    """Набор всех настроек"""
    database_settings: DatabaseSettings

@lru_cache
def init_settings() -> Settings:
    return Settings(database_settings=DatabaseSettings())


settings = init_settings()
