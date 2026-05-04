from pydantic import BaseModel
from datetime import date
from Entidades.detalle_recepcion_schema import DetalleRecepcionCreate

class RecepcionCompleta(BaseModel):
    embarque_id: int
    fecha_recepcion: date
    detalles: list[DetalleRecepcionCreate]