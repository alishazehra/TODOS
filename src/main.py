
# src/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from core.config import settings
from src.db.connection import engine  # <-- FIXED: import the engine
from src.api import auth, todos
from src.models import *  # import your models so tables are created

# Lifespan context for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create tables if they don't exist
    SQLModel.metadata.create_all(engine, checkfirst=True)
    print("✅ Database tables created")
    yield
    # Shutdown: cleanup if needed


# Create FastAPI app
app = FastAPI(
    title="Evolution of Todo API",
    description="Phase II Full-Stack Todo Web Application API",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://todos-2her.vercel.app/signup",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(todos.router, prefix="/api/v1/todos", tags=["todos"])

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Root endpoint
@app.get("/")
async def root():
    return {
        "name": "Evolution of Todo API",
        "version": "1.0.0",
        "docs": "/docs",
    }
