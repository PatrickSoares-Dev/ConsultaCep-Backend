from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    hash = Column(String, nullable=False, unique=True) 
    full_name = Column(String, nullable=False)

    addresses = relationship("Address", back_populates="user")

    credito = relationship("ConsultaCredito", uselist=False, back_populates="user")
