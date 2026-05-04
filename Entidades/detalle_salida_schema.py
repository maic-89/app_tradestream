from pydantic import BaseModel

class DetalleSalidaSchema(BaseModel):
    id_salida: int
    id_producto: int
    cantidad: int