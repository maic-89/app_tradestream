from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(50), nullable=False)
    contrasena = Column(String(100), nullable=False)
    nombre = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    rol = Column(String(20), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    edad = Column(Integer, nullable=False)
    direccion = Column(String(100), nullable=False)
    