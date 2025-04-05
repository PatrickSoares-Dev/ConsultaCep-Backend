from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas import user_schema
from ..services import auth_service
from ..database import get_db

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/register", response_model=user_schema.UserResponse)
def register(user_data: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = auth_service.create_user(user_data, db)
    return db_user


@router.post("/login")
def login(credentials: user_schema.UserLogin, db: Session = Depends(get_db)):
    auth_data = auth_service.authenticate_user(credentials, db)
    if not auth_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )
    return {
        "success": True,
        "status_code": 200,
        "data": auth_data
    }
