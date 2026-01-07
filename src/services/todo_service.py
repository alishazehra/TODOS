from sqlmodel import Session, select
from fastapi import HTTPException, status
from typing import List
from ..models.todo import Todo


class TodoService:
    """Service for todo-related operations"""

    @staticmethod
    def list_todos_by_user(db: Session, user_id: str) -> List[Todo]:
        """List all todos for a user, ordered by creation date (newest first)"""
        todos = db.exec(
            select(Todo)
            .where(Todo.user_id == user_id)
            .order_by(Todo.created_at.desc())
        ).all()
        return todos

    @staticmethod
    def get_todo_by_id(db: Session, todo_id: str, user_id: str) -> Todo | None:
        """Get a todo by ID, ensuring it belongs to the user"""
        todo = db.get(Todo, todo_id)
        if todo is None:
            return None
        if todo.user_id != user_id:
            return None
        return todo

    @staticmethod
    def create_todo(db: Session, user_id: str, description: str) -> Todo:
        """Create a new todo for a user"""
        todo = Todo(user_id=user_id, description=description)
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return todo

    @staticmethod
    def update_todo(
        db: Session, todo_id: str, user_id: str, description: str | None = None, completed: bool | None = None
    ) -> Todo:
        """Update a todo, ensuring it belongs to the user"""
        todo = TodoService.get_todo_by_id(db, todo_id, user_id)
        if todo is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found",
            )

        if description is not None:
            todo.description = description
        if completed is not None:
            todo.completed = completed

        db.commit()
        db.refresh(todo)
        return todo

    @staticmethod
    def delete_todo(db: Session, todo_id: str, user_id: str) -> bool:
        """Delete a todo, ensuring it belongs to the user"""
        todo = TodoService.get_todo_by_id(db, todo_id, user_id)
        if todo is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found",
            )

        db.delete(todo)
        db.commit()
        return True

    @staticmethod
    def toggle_todo(db: Session, todo_id: str, user_id: str) -> Todo:
        """Toggle the completed status of a todo"""
        todo = TodoService.get_todo_by_id(db, todo_id, user_id)
        if todo is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found",
            )

        todo.completed = not todo.completed
        db.commit()
        db.refresh(todo)
        return todo
