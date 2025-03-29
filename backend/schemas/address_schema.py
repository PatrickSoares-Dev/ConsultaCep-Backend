from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CepRequest(BaseModel):
    cep: str


class AddressResponse(BaseModel):
    id: int
    cep: str
    logradouro: Optional[str]
    complemento: Optional[str]
    bairro: Optional[str]
    localidade: Optional[str]
    uf: Optional[str]
    data_consulta: datetime

    class Config:
        orm_mode = True
