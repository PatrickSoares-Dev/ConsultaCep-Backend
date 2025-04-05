from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Float
from sqlalchemy.orm import relationship
from ..database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    cep = Column(String(9), nullable=False)
    logradouro = Column(String)
    complemento = Column(String)
    bairro = Column(String)
    localidade = Column(String)
    uf = Column(String)
    data_consulta = Column(DateTime, server_default=func.now())
    credito_utilizado = Column(Float, default=0.02)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="addresses")