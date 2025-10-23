from functools import lru_cache
from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # JWT Stuff
    JWT_SECRET_KEY: Optional[str] = None
    JWT_ALGORITHM: Optional[str] = None
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080

    # MongoDB Stuff
    MONGO_URI: Optional[str] = None
    DB_NAME: Optional[str] = None
    USERS_COLLECTION: str = "Users"

    # Configure code to read from .env file in the backend dir
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return cached settings loaded from environment/.env."""
    return Settings()
