from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    proveedor_id = Column(Integer, ForeignKey("proveedores.id"), nullable=False)
    bodega_destino = Column(String(100), nullable=False)
    precio_total = Column(Float, nullable=False)
    estado = Column(String(50), default="pendiente")
    fecha_pedido = Column(DateTime(timezone=True), server_default=func.now())
    fecha_entrega = Column(DateTime(timezone=True), nullable=True)


  
    usuario = relationship("Usuario")
    proveedor = relationship("Proveedor", back_populates="pedidos")
    detalles_pedido = relationship("DetallePedido", back_populates="pedido", cascade="all, delete-orphan")
    embarque = relationship("Embarque", uselist=False, back_populates="pedido")
    recepcion = relationship("Recepcion", uselist=False, back_populates="pedido")