from fastapi.security  import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from jose import jwt
from requests import Session
from database import get_db
from auth_servicio import login

router = APIRouter(prefix="/aut", tags=["Auth"])

@router.post("/login")
def login_user(data: dict, db: Session = Depends(get_db)):

    return login(db, data["username"], data["password"])
