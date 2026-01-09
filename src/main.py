
# src/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from core.config import settings
from src.db.connection import engine
from src.api import auth, todos
from src.models import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine, checkfirst=True)
    print("✅ Database tables created")
    yield

app = FastAPI(
    title="Evolution of Todo API",
    description="Phase II Full-Stack Todo Web Application API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://todos-2her.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(todos.router, prefix="/api/v1/todos", tags=["todos"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def root():
    return {
        "name": "Evolution of Todo API",
        "version": "1.0.0",
        "docs": "/docs",
    }
