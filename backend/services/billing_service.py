from sqlalchemy.orm import Session
from ..models.billing import ConsultaCredito
from ..models.user import User

def get_credito(db: Session, user: User) -> ConsultaCredito:
    credito = db.query(ConsultaCredito).filter_by(user_id=user.id).first()
    if not credito:
        credito = ConsultaCredito(user_id=user.id)
        db.add(credito)
        db.commit()
        db.refresh(credito)
    return credito

def adicionar_credito(db: Session, user: User, valor: float):
    credito = get_credito(db, user)
    credito.saldo += valor
    db.commit()
    return credito

def alterar_saldo(db: Session, user: User, novo_saldo: float):
    credito = get_credito(db, user)
    credito.saldo = novo_saldo
    db.commit()
    return credito

def remover_credito(db: Session, user: User, valor: float):
    credito = get_credito(db, user)
    if credito.saldo < valor:
        raise ValueError("Saldo insuficiente para remover esse valor")
    
    credito.saldo -= valor
    credito.total_usado += valor
    db.commit()
    return credito
