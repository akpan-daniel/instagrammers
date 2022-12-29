import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str = os.environ.get("DB_HOST")
    db_user: str = os.environ.get("DB_USER")
    db_port: str = os.environ.get("DB_PORT")
    db_pass: str = os.environ.get("DB_PASS")
    db_name: str = os.environ.get("DB_NAME")
    secret_key: str = os.environ.get("SECRET_KEY")
    test_user_email: str | None = os.environ.get("TEST_USER_EMAIL")
    test_user_password: str | None = os.environ.get("TEST_USER_PASSWORD")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
