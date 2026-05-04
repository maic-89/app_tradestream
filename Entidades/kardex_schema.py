from pydantic import BaseModel
from datetime import datetime

class kardexResponse(BaseModel):
    id: int
    id_producto: int
    tipo_movimiento: str
    cantidad: int
    stock_anterior: int
    stock_actual: int
    costo_unitario: int
    saldo_valorizado: int
    referencia: str
    fecha_movimiento: datetime

    class config:
        from_attribute = True