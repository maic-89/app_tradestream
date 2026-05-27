from fastapi import APIRouter, HTTPException, Depends, status, Body
from sqlalchemy.orm import Session
from database import SessionLocal
from usuario_schema import UsuarioCreate, UsuarioResponse, login_usuario as LoginSchema
from usuario_servicio import crear_usuario_servicio, listar_usuario_servicio, login_usuario as login_func

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login_endpoint(datos: LoginSchema = Body(...), db: Session = Depends(get_db)):
    resultado = login_func(db, datos.usuario, datos.contrasena)
   
    if not resultado:
        raise HTTPException(
            status_code=401, 
            detail="Credenciales inválidas"
            )
    
    return resultado

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario_servicio(db, usuario)

@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return listar_usuario_servicio(db)