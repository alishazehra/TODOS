import pytest
from httpx import AsyncClient, ASGITransport
from sqlmodel import SQLModel, create_engine, Session
from sqlmodel.pool import StaticPool

# Create in-memory SQLite database for testing
test_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


@pytest.fixture(scope="function")
def test_db():
    """Create and drop tables for each test"""
    SQLModel.metadata.create_all(test_engine)
    yield test_engine
    SQLModel.metadata.drop_all(test_engine)


@pytest.fixture
def client(test_db):
    """Create a test client"""
    # Import app here to avoid circular imports
    from src.main import app
    from src.db.connection import get_db

    def override_get_db():
        with Session(test_db) as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db

    transport = ASGITransport(app=app)
    with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

    app.dependency_overrides.clear()
