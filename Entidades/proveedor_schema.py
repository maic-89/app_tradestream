from pydantic import BaseModel

class ProveedorBase(BaseModel):
    id: int
    nombre: str
    nit: str
    razon_social: str
    direccion: str
    telefono: str
    email: str

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorResponse(ProveedorBase):
    id: int

    class Config:
        from_attributes = True