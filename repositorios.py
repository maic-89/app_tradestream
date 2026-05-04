from sqlalchemy.orm import Session
from usuario_db import Usuario

def crear_usuario(db: Session, usuario: Usuario):
    db_usuario = Usuario(
        usuario=usuario.usuario,
        contrasena=usuario.contrasena,
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        correo=usuario.correo,
        edad=usuario.edad,
        direccion=usuario.direccion
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def obtener_usuario_por_username(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == Usuario).first()