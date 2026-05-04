from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Embarque(Base):
    __tablename__ = "embarques"

    id = Column(Integer, primary_key=True, index=True)

    fecha_embarque = Column(DATE, nullable=False)
    destino = Column(String, nullable=False)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)

    fecha_llegada_estimada = Column(DATE, nullable=False)
    fecha_llegada_real = Column(DATE, nullable=True)

    estado = Column(String(50),default="En tránsito")
    numero_guia = Column(String(100))
    pedido = relationship("Pedido", back_populates="embarque")