from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class DetalleSalida(Base):
    __tablename__ = "detalle_salida"
    
    id = Column(Integer, primary_key=True, index=True)
    id_salida = Column(Integer, ForeignKey("salida.id"))
    id_producto = Column(Integer, ForeignKey("producto.id"))
    cantidad = Column(Integer)