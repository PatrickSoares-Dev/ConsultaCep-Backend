from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas import user_schema
from ..models.user import User
from ..database import get_db
from ..services import auth_service

router = APIRouter(prefix="/users", tags=["Usuários"])


@router.get("/", response_model=list[user_schema.UserResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get("/{user_id}", response_model=user_schema.UserResponse)
def obter_usuario(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user


@router.post("/", response_model=user_schema.UserResponse)
def criar_usuario(dados: user_schema.UserCreate, db: Session = Depends(get_db)):
    return auth_service.create_user(dados, db)


@router.put("/{user_id}", response_model=user_schema.UserResponse)
def atualizar_usuario(user_id: int, dados: user_schema.UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    user.email = dados.email
    user.full_name = dados.full_name
    user.hashed_password = auth_service.get_password_hash(dados.password)
    db.commit()
    db.refresh(user)
    return user


@router.delete("/{user_id}")
def deletar_usuario(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(user)
    db.commit()
    return {"detail": "Usuário deletado com sucesso"}
