from pydantic import BaseModel
from datetime import date
from Entidades.detalle_salida_schema import DetalleSalidaSchema

class SalidaCompletaSchema(BaseModel):
    fecha: date
    detalles: list[DetalleSalidaSchema]

