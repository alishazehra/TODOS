from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    """Schema for user registration request"""
    email: EmailStr = Field(..., max_length=255, description="User's email address")
    password: str = Field(..., min_length=8, max_length=72, description="User's password (min 8, max 72 characters)")
    confirm_password: str = Field(..., min_length=8, max_length=72, description="Password confirmation")

    def validate_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self


class UserLogin(BaseModel):
    """Schema for user login request"""
    email: EmailStr = Field(..., max_length=255, description="User's email address")
    password: str = Field(..., max_length=72, description="User's password")


class UserResponse(BaseModel):
    """Schema for user response"""
    id: str
    email: str
    createdAt: datetime
    updatedAt: datetime

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    """Schema for token response"""
    token: str
    expiresAt: datetime


class AuthResponse(BaseModel):
    """Schema for authentication response"""
    user: UserResponse
    session: TokenResponse


class ErrorResponse(BaseModel):
    """Schema for error response"""
    error: dict
