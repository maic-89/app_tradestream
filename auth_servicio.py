from sqlalchemy.orm import Session
from fastapi import HTTPException
from usuario_db import Usuario
from security import verify_password, create_access_token

def login(db: Session, username: str, password: str):
    user = db.query(Usuario).filter(Usuario.username == username).first()
    
    
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
    
    token = create_access_token(data={"sub": user.username})

    return {"access_token": token, "token_type": "bearer"}