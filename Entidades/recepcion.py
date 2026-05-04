from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Recepcion(Base):
    __tablename__ = "recepcion_mercancia"

    id = Column(Integer, primary_key=True, index=True)
    fecha_recepcion = Column(Date, nullable=False)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    
    pedido = relationship("Pedido", back_populates="recepcion")
    DetalleRecepcion = relationship("DetalleRecepcion", back_populates="recepcion")