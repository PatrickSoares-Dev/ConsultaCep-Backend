from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import address_schema
from ..services import cep_service
from ..security import get_current_user
from ..database import get_db
from ..models.user import User
from ..models.address import Address

router = APIRouter(prefix="/cep", tags=["Consulta CEP"])


@router.get("/historico", response_model=list[address_schema.AddressResponse])
def historico(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return cep_service.historico_por_usuario(db, user)


@router.get("/{cep}", response_model=address_schema.AddressResponse)
def consultar_cep(cep: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    result = cep_service.buscar_cep(cep, db, user)
    if not result:
        raise HTTPException(status_code=404, detail="CEP não encontrado")
    return result


@router.delete("/historico/{cep}")
def deletar_cep_do_historico(cep: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    address = db.query(Address).filter(Address.cep == cep, Address.user_id == user.id).first()
    if not address:
        raise HTTPException(status_code=404, detail="CEP não encontrado no histórico")
    
    db.delete(address)
    db.commit()
    return {"detail": "CEP removido do histórico"}
