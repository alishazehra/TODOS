from sqlmodel import Session, select
from fastapi import HTTPException, status
from ..models.user import User
from ..core.security import hash_password


class UserService:
    """Service for user-related operations"""

    @staticmethod
    def create_user(db: Session, email: str, password: str) -> User:
        """
        Create a new user account.

        Args:
            db: Database session
            email: User's email address
            password: User's plaintext password

        Returns:
            Created User object

        Raises:
            HTTPException: If email already exists
        """
        # Check if user already exists
        existing = db.exec(select(User).where(User.email == email)).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )

        # Create new user
        hashed = hash_password(password)
        user = User(email=email, hashed_password=hashed)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User | None:
        """Get a user by email address"""
        return db.exec(select(User).where(User.email == email)).first()

    @staticmethod
    def get_user_by_id(db: Session, user_id: str) -> User | None:
        """Get a user by ID"""
        return db.get(User, user_id)

    @staticmethod
    def verify_password(db: Session, email: str, password: str) -> User | None:
        """
        Verify user credentials.

        Args:
            db: Database session
            email: User's email
            password: Plaintext password to verify

        Returns:
            User if credentials valid, None otherwise
        """
        from ..core.security import verify_password

        user = UserService.get_user_by_email(db, email)
        if user is None:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
