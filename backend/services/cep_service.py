import requests
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.address import Address
from ..models.user import User
from ..services import billing_service


def buscar_cep(cep: str, db: Session, user: User) -> Address | None:
    cep = cep.strip().replace("-", "")

    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if response.status_code != 200 or "erro" in response.json():
        return None

    data = response.json()
    cep_formatado = data.get("cep") 

    existente = db.query(Address).filter(Address.cep == cep_formatado, Address.user_id == user.id).first()
    if existente:
        return existente

    credito = billing_service.get_credito(db, user)
    if credito.saldo < 0.02:
        raise HTTPException(status_code=402, detail="Créditos insuficientes para consulta")
    
    credito.saldo -= 0.02
    credito.total_usado += 0.02
    credito.total_consultas += 1

    address = Address(
        cep=cep_formatado,
        logradouro=data.get("logradouro"),
        complemento=data.get("complemento"),
        bairro=data.get("bairro"),
        localidade=data.get("localidade"),
        uf=data.get("uf"),
        user_id=user.id
    )

    db.add(address)
    db.commit()
    db.refresh(address)

    return address

def historico_por_usuario(db: Session, user: User) -> list[Address]:
    return (
        db.query(Address)
        .filter(Address.user_id == user.id)
        .order_by(Address.data_consulta.desc())
        .all()
    )