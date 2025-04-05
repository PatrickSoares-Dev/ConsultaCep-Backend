from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CepRequest(BaseModel):
    cep: str

class AddressResponse(BaseModel):
    id: int
    cep: str
    logradouro: str | None
    complemento: str | None
    bairro: str | None
    localidade: str | None
    uf: str | None
    data_consulta: datetime
    credito_utilizado: float 

    class Config:
        from_attributes = True

