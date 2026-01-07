from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class TodoCreate(BaseModel):
    """Schema for creating a todo"""
    description: str = Field(..., min_length=1, max_length=1000, description="Todo description")


class TodoUpdate(BaseModel):
    """Schema for updating a todo"""
    description: Optional[str] = Field(None, min_length=1, max_length=1000)
    completed: Optional[bool] = None


class TodoResponse(BaseModel):
    """Schema for todo response"""
    id: str
    userId: str
    description: str
    completed: bool
    createdAt: datetime
    updatedAt: datetime

    model_config = ConfigDict(from_attributes=True)


class TodoListResponse(BaseModel):
    """Schema for todo list response"""
    todos: list[TodoResponse]
