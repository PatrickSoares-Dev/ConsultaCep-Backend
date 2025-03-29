from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..security import get_current_user
from ..models.user import User
from ..schemas.billing_schema import CreditoResponse, CreditoBase, CreditoUpdate
from ..services import billing_service

router = APIRouter(prefix="/billing", tags=["Billing"])


@router.get("/", response_model=CreditoResponse)
def consultar_creditos(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return billing_service.get_credito(db, user)


@router.post("/adicionar", response_model=CreditoResponse)
def adicionar_creditos(body: CreditoBase, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return billing_service.adicionar_credito(db, user, body.saldo)


@router.put("/alterar", response_model=CreditoResponse)
def alterar_credito(body: CreditoUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return billing_service.alterar_saldo(db, user, body.saldo)


@router.put("/remover", response_model=CreditoResponse)
def remover_credito(body: CreditoBase, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        return billing_service.remover_credito(db, user, body.saldo)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
