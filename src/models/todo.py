from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid


class Todo(SQLModel, table=True):
    """
    Todo entity representing a task to be completed.
    Each todo belongs to exactly one user.
    """
    __tablename__ = "todos"

    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        max_length=36
    )
    user_id: str = Field(
        foreign_key="users.id",
        index=True,
        max_length=36
    )
    description: str = Field(max_length=1000)
    completed: bool = Field(default=False, nullable=False)
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )

    def __repr__(self):
        return f"<Todo(id={self.id}, description={self.description[:20]}..., completed={self.completed})>"
