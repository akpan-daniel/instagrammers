import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.models import Base
from app.routers.dependencies import get_db

DATABASE_URL = "sqlite:///./test.sqlite3"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_test_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module", name="client")
def test_app():
    Base.metadata.create_all(engine)
    app.dependency_overrides[get_db] = get_test_db
    client = TestClient(app)
    yield client

    Base.metadata.drop_all(engine)
