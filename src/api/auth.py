from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlmodel import Session
from pydantic import EmailStr
from datetime import timedelta

from ..db.connection import get_db
from ..core.config import get_settings
from ..core.security import create_access_token
from ..schemas.user import UserCreate, UserLogin, UserResponse, AuthResponse, ErrorResponse
from ..services.user_service import UserService
from .deps import get_current_user
from ..models.user import User

settings = get_settings()

router = APIRouter()


@router.post(
    "/signup",
    response_model=AuthResponse,
    responses={
        409: {"model": ErrorResponse, "description": "Email already registered"},
        422: {"model": ErrorResponse, "description": "Validation error"},
    },
    summary="Register a new user",
    description="Create a new user account with email and password",
)
async def signup(
    response: Response,
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    """
    Register a new user account.

    - **email**: Valid email address (must be unique)
    - **password**: Minimum 8 characters
    - **confirm_password**: Must match password
    """
    # Validate passwords match
    if user_data.password != user_data.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"error": {"code": "VALIDATION_ERROR", "message": "Passwords do not match"}},
        )

    # Create user
    try:
        user = UserService.create_user(db, user_data.email, user_data.password)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"error": {"code": "VALIDATION_ERROR", "message": str(e)}},
        )

    # Create session token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    token = create_access_token(user.id, access_token_expires)

    return AuthResponse(
        user=UserResponse(
            id=user.id,
            email=user.email,
            createdAt=user.created_at,
            updatedAt=user.updated_at,
        ),
        session={"token": token, "expiresAt": user.created_at + access_token_expires},
    )


@router.post(
    "/signin",
    response_model=AuthResponse,
    responses={
        401: {"model": ErrorResponse, "description": "Invalid credentials"},
        422: {"model": ErrorResponse, "description": "Validation error"},
    },
    summary="Sign in a user",
    description="Authenticate user with email and password",
)
async def signin(
    response: Response,
    credentials: UserLogin,
    db: Session = Depends(get_db),
):
    """
    Sign in with email and password.

    - **email**: Registered email address
    - **password**: Account password
    """
    user = UserService.verify_password(db, credentials.email, credentials.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": {"code": "INVALID_CREDENTIALS", "message": "Invalid email or password"}},
        )

    # Create session token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    token = create_access_token(user.id, access_token_expires)

    return AuthResponse(
        user=UserResponse(
            id=user.id,
            email=user.email,
            createdAt=user.created_at,
            updatedAt=user.updated_at,
        ),
        session={"token": token, "expiresAt": user.created_at + access_token_expires},
    )


@router.post(
    "/signout",
    summary="Sign out a user",
    description="End the current user session",
    responses={
        200: {"description": "Successfully signed out"},
    },
)
async def signout(response: Response):
    """Sign out the current user"""
    # In a more sophisticated implementation, you would invalidate the token
    # For now, we just return success
    return {"message": "Successfully signed out"}


@router.get(
    "/me",
    response_model=UserResponse,
    responses={
        401: {"model": ErrorResponse, "description": "Not authenticated"},
    },
    summary="Get current user",
    description="Get the currently authenticated user's information",
)
async def get_me(current_user: User = Depends(get_current_user)):
    """Get current authenticated user"""
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        createdAt=current_user.created_at,
        updatedAt=current_user.updated_at,
    )
