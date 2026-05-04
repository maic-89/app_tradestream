from sqlalchemy import Column, Integer, Date
from database import Base

class Salida(Base):
    __tablename__ = "salida_mercancia"
    
    id = Column(Integer, primary_key=True, index=True)
    fecha_salida = Column(Date)