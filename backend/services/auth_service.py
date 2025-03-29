from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import secrets

from ..models.user import User
from ..schemas.user_schema import UserCreate, UserLogin
from ..core.config import settings  # ✅ CORRETO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def create_user(user_data: UserCreate, db: Session) -> User:
    hashed_password = get_password_hash(user_data.password)
    user_hash = secrets.token_hex(16)

    user = User(
        email=user_data.email,
        hashed_password=hashed_password,
        hash=user_hash,
        full_name=user_data.full_name
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(credentials: UserLogin, db: Session) -> str | None:
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        return None
    return create_access_token({"sub": str(user.id)})
