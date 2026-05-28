from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
#from repositorios import obtener_usuario_por_username
from usuario_schema import UsuarioCreate, UsuarioResponse
from usuario_servicio import crear_usuario_servicio, listar_usuario_servicio
from validar_token import obtener_usuario_por_actual


router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuarios: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario_servicio(db, usuarios)

@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return listar_usuario_servicio(db)

@router.get("/perfil")
def perfil(usuario: str = Depends(obtener_usuario_por_actual), db: Session = Depends(get_db)):
    return {"usuario": usuario}
        
#@router.post("/login")
#def login(usuario: login_usuario, db: Session = Depends(get_db)):
#    resultado = login_usuario(db, usuario.usuario, usuario.contrasena)

#    if not resultado:
#        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
#    
#    return resultado
    



