
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from .core.config import settings
from .db.connection import engine
from .api import auth, todos


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create tables if they don't exist
    SQLModel.metadata.create_all(engine, checkfirst=True)
    yield
    # Shutdown: cleanup if needed


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
        "https://todos-2her.vercel.app/signup",  # Your deployed frontend URL
        "http://localhost:3000",          # For local testing
        "http://127.0.0.1:3000"           # Another local testing URL
    ],
    allow_credentials=True,  # Needed for cookies or authorization headers
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],     # Allow all headers
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(todos.router, prefix="/api/v1/todos", tags=["todos"])


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "Evolution of Todo API",
        "version": "1.0.0",
        "docs": "/docs",
    }
