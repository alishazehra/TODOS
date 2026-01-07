from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid


class User(SQLModel, table=True):
    """
    User entity representing a registered user account.
    Users own zero or more todos.
    """
    __tablename__ = "users"
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        max_length=36
    )
    email: str = Field(
        unique=True,
        index=True,
        max_length=255
    )
    hashed_password: str = Field(max_length=255)
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
