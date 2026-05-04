from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base

class Inventario(Base):
    __tablename__ = "inventarios"
    
    id = Column(Integer, primary_key=True, index=True)
    bodega = Column(String(100), nullable=False)
    referencia = Column(String(255), nullable=True)  # Referencia al pedido o embarque

    cantidad = Column(Integer, nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"))
    stock_minimo = Column(Integer, default=5)
    detalles = Column(String(255), nullable=True)  # Detalles adicionales sobre el inventario
    notas = Column(String(255), nullable=True)  # Notas adicionales sobre el inventario
    
    producto = relationship("Producto", back_populates="inventarios")

    