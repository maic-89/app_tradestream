from pydantic import BaseModel
from Entidades.detalle_pedido_schema import DetallePedido


class PedidoCreate(BaseModel):
    proveedor: int
    detalles: list[DetallePedido]