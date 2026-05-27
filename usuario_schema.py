from pydantic import BaseModel


class UsuarioCreate(BaseModel):
    usuario: str
    contrasena: str
    nombre: str
    apellidos: str
    correo: str
    edad: int
    direccion: str

class UsuarioResponse(BaseModel):
        id: int
        nombre: str
        correo: str

        class Config:
            from_attributes = True

class login_usuario(BaseModel):
    usuario: str
    contrasena: str

    class Config:
        from_attributes = True