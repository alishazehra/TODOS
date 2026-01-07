from sqlmodel import create_engine, SQLModel, Session
from ..core.config import settings

# Create engine for Neon PostgreSQL
engine = create_engine(
    settings.database_url,
    echo=False,
    pool_pre_ping=True,
)


def get_db():
    """Dependency for getting database session"""
    with Session(engine) as session:
        yield session
