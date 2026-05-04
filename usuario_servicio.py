from auth import crear_token_acceso
from security import verify_password, hash_password
from repositorios import obtener_usuario_por_username, crear_usuario, listar_usuarios 


def crear_usuario_servicio(db, usuario):

    usuario.contrasena = hash_password(usuario.contrasena)
    return crear_usuario(db, usuario)

def listar_usuario_servicio(db):
    return listar_usuarios(db)

def login_usuario(db, username: str, contrasena: str):
    usuario_db = obtener_usuario_por_username(db, username)
    
    if not usuario_db:
        return None
    
    if not verify_password(contrasena, usuario_db.contrasena):
        return None

    token = crear_token_acceso({
        "sub": usuario_db.usuario,
        "rol": usuario_db.rol
        })
    return {"access_token": token, 
            "token_type": "bearer"
            }

