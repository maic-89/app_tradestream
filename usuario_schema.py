from pydantic import BaseModel


class UsuarioCreate(BaseModel):
    usuario: str
    contrasena: str
    nombre: str
    apellidos: str
    correo: str
    edad: str
    direccion: str

class UsuarioResponse(BaseModel):
        id: int
        nombre: str
        correo: str

        class Config:
            from_atributes = True

class login_usuario(BaseModel):
    usuario: str
    contrasena: str