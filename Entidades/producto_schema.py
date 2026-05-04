from pydantic import BaseModel

class PruductBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    proveedor_id: int

class ProductoCreate(PruductBase):
    pass

class Producto(PruductBase):
    id: int

    class Config:
       from_atributes = True