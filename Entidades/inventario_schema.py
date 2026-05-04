from pydantic import BaseModel, ConfigDict

class InventarioResponse(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    ubicacion: str | None = None
    stock_minimo: int

    model_config = ConfigDict(from_attributes=True)

class InventarioAlertasResponse(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    ubicacion: str
    stock_minimo:int

    model_config = ConfigDict(from_attributes=True)