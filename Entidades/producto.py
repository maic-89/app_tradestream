from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base
from sqlalchemy.orm import relationship



class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    valor_neto = Column(Float, nullable=False)
    valor_bruto = Column(Float, nullable=False)
    impuestos = Column(Float, nullable=False)
    proveedor_id = Column(Integer, ForeignKey("proveedores.id"), nullable=False)

    detalle_pedido = relationship("DetallePedido", back_populates="producto")
    proveedor = relationship("Proveedor", back_populates="productos")
    detalles_recepcion = relationship("DetalleRecepcion", back_populates="producto")
    inventarios = relationship("Inventario", back_populates="producto")
    kardex = relationship("Kardex", back_populates="producto")
    
