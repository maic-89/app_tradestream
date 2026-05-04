from pydantic import BaseModel
from datetime import datetime
from Entidades.detalle_pedido_schema import DetallePedidoCreate

class PedidoBase(BaseModel):
    proveedor: int
    id_producto: int
    cantidad: int
    fecha_pedido: datetime

class PedidoCreate(PedidoBase):
    detalles: list[DetallePedidoCreate]

class PedidoResponse(PedidoBase):
    id: int
    precio_total: float
    estado: str

    class Config:
        from_atributes = True