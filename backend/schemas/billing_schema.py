from pydantic import BaseModel

class CreditoBase(BaseModel):
    saldo: float

class CreditoUpdate(CreditoBase):
    pass

class CreditoResponse(BaseModel):
    saldo: float
    total_usado: float
    total_consultas: int

    class Config:
        from_attributes = True
