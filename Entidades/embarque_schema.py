from pydantic import BaseModel
from datetime import datetime

class EmbarqueBase(BaseModel):

    pedido_id: int
    fecha_salida: datetime
    fecha_llegada_estimada: datetime
    fecha_llegada_real: datetime | None = None
    estado: str
    tipo_transporte: str

class EmbarqueCreate(EmbarqueBase):
    pass

class EmbarqueResponse(EmbarqueBase):
    id: int

    class Config:
        from_attributes = True