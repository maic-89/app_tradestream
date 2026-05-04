from auth import ALGORITHM, SECRET_KEY
from security import verify_password
from repositorios import obtener_usuario_por_username
from usuario_db import Usuario   
from jose import jwt

def login_usuario(db, session_usuario: str, contrasena: str):
    usuario = db.query(Usuario).filter(Usuario.usuario == session_usuario).first()

    if not usuario:
        return None
    
    if not verify_password(contrasena, usuario.contrasena):
        return None
    
    token = jwt.encode(
        {"sub": usuario.usuario, "rol": usuario.rol}, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}