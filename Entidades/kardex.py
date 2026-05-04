from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Kardex(Base):
    __tablename__ = 'kardex'
    
    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey('productos.id'))
    usuario = Column(String, nullable=False)

    tipo_movimiento = Column(String, nullable=False)  # 'entrada' o 'salida'
    cantidad_entrada = Column(Integer, default=0)
    cantidad_salida = Column(Integer, default=0)

    referencia = Column(String, nullable=True)  # Referencia al pedido o embarque
    fecha_movimiento = Column(DateTime, default=datetime.utcnow)
    
    producto = relationship("Producto", back_populates="kardex")
    
    stock_anterior = Column(Integer)
    cantidad = Column(Integer)
    stock_actual = Column(Integer)

    tipo_documento = Column(String, nullable=False)  # 'pedido', 'embarque', 'recepcion', 'salida'
    documento_id = Column(Integer, nullable=False)  # ID del documento relacionado (pedido_id, embarque_id, etc.)

    costo_unitario = Column(Integer, nullable=True)  # Costo unitario del producto en este movimiento
    saldo_valorizado = Column(Integer, nullable=True)  # Saldo valorizado después de este movimiento


    producto = relationship("Producto", back_populates="kardex")