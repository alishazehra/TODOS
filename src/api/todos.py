from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.responses import JSONResponse
from sqlmodel import Session
from typing import List

from src.db.connection import get_db

from ..schemas.todo import TodoCreate, TodoUpdate, TodoResponse, TodoListResponse
from ..services.todo_service import TodoService
from .deps import get_current_user
from ..models.user import User

router = APIRouter()


@router.get(
    "",
    response_model=TodoListResponse,
    summary="List all todos",
    description="Retrieve all todos for the authenticated user",
)
async def list_todos(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List all todos for the current user"""
    todos = TodoService.list_todos_by_user(db, current_user.id)
    # Convert Todo objects to TodoResponse with camelCase fields
    todo_responses = [
        TodoResponse(
            id=todo.id,
            userId=todo.user_id,
            description=todo.description,
            completed=todo.completed,
            createdAt=todo.created_at,
            updatedAt=todo.updated_at,
        )
        for todo in todos
    ]
    return TodoListResponse(todos=todo_responses)


@router.post(
    "",
    response_model=None,
    responses={
        422: {"description": "Validation error"},
    },
    summary="Create a todo",
    description="Create a new todo for the authenticated user",
)
async def create_todo(
    todo_data: TodoCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new todo"""
    todo = TodoService.create_todo(db, current_user.id, todo_data.description)
    # Return as {"todo": ...} to match frontend expectations
    return JSONResponse(content={
        "id": todo.id,
        "userId": todo.user_id,
        "description": todo.description,
        "completed": todo.completed,
        "createdAt": todo.created_at.isoformat(),
        "updatedAt": todo.updated_at.isoformat(),
    })


@router.get(
    "/{todo_id}",
    response_model=TodoResponse,
    responses={
        404: {"description": "Todo not found"},
    },
    summary="Get a todo",
    description="Retrieve a specific todo by ID",
)
async def get_todo(
    todo_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get a specific todo"""
    todo = TodoService.get_todo_by_id(db, todo_id, current_user.id)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": {"code": "NOT_FOUND", "message": "Todo not found"}},
        )
    return TodoResponse(
        id=todo.id,
        userId=todo.user_id,
        description=todo.description,
        completed=todo.completed,
        createdAt=todo.created_at,
        updatedAt=todo.updated_at,
    )


@router.put(
    "/{todo_id}",
    response_model=TodoResponse,
    responses={
        404: {"description": "Todo not found"},
    },
    summary="Update a todo",
    description="Update an existing todo's description",
)
async def update_todo(
    todo_id: str,
    todo_data: TodoUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update a todo"""
    todo = TodoService.update_todo(
        db,
        todo_id,
        current_user.id,
        description=todo_data.description,
        completed=todo_data.completed,
    )
    return TodoResponse(
        id=todo.id,
        userId=todo.user_id,
        description=todo.description,
        completed=todo.completed,
        createdAt=todo.created_at,
        updatedAt=todo.updated_at,
    )


@router.delete(
    "/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"description": "Todo not found"},
    },
    summary="Delete a todo",
    description="Delete a todo permanently",
)
async def delete_todo(
    todo_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a todo"""
    TodoService.delete_todo(db, todo_id, current_user.id)
    return None


@router.patch(
    "/{todo_id}/toggle",
    response_model=TodoResponse,
    responses={
        404: {"description": "Todo not found"},
    },
    summary="Toggle todo completion",
    description="Toggle a todo between complete and incomplete status",
)
async def toggle_todo(
    todo_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Toggle todo completion status"""
    todo = TodoService.toggle_todo(db, todo_id, current_user.id)
    return TodoResponse(
        id=todo.id,
        userId=todo.user_id,
        description=todo.description,
        completed=todo.completed,
        createdAt=todo.created_at,
        updatedAt=todo.updated_at,
    )
