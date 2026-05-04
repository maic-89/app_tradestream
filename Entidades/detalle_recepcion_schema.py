from pydantic import BaseModel

class DetalleRecepcionCreate(BaseModel):
    producto_id: int
    cantidad_recibida: int