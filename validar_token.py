from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from auth import ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuarios/login")

def obtener_usuario_por_actual(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario = payload.get("sub")
        
        if usuario is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        
        return usuario
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")