from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class DetalleRecepcion(Base):
    __tablename__ = "detalle_recepciones"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    recepcion_id = Column(Integer, ForeignKey("recepcion_mercancia.id"), nullable=False)
    detalle_pedido_id = Column(Integer, ForeignKey("detalle_pedidos.id"), nullable=False)
    
    cantidad_recibida = Column(Integer, nullable=False)
    
    producto = relationship("Producto", back_populates="detalles_recepcion")
    recepcion = relationship("Recepcion", back_populates="DetalleRecepcion")