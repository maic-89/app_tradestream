from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class Proveedor(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    nit = Column(String(20), unique=True, nullable=False)
    razon_social = Column(String(100), nullable=False)
    direccion = Column(String(255), nullable=False)
    telefono = Column(String(20))
    email = Column(String(100))


    productos = relationship("Producto", back_populates="proveedor")
    pedidos = relationship("Pedido", back_populates="proveedor")