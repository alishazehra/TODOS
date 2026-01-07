from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Database
    database_url: str

    # Authentication
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 10080  # 7 days

    # Server
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
