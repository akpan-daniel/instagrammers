from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.config.db import Base
from app.utils.users import hash_password, verify_password


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    followers = Column(Integer, default=0)
    bio = Column(String, default="")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def make_password(self, password: str):
        self.password = hash_password(password)

    def is_password(self, password: str):
        return verify_password(password, self.password)
