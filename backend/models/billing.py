from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class ConsultaCredito(Base):
    __tablename__ = "consulta_creditos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    saldo = Column(Float, default=0.0)
    total_usado = Column(Float, default=0.0)
    total_consultas = Column(Integer, default=0)

    user = relationship("User", back_populates="credito")

