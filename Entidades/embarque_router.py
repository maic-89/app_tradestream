from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from Entidades.embarque_schema import EmbarqueCreate, EmbarqueResponse
from Entidades.embarque_servicio import crear_embarque_servicio, listar_embarques_servicio

router = APIRouter(prefix="/embarques", tags=["Embarques"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EmbarqueResponse)
def crear_embarque(embarque: EmbarqueCreate, db: Session = Depends(get_db)):
    return crear_embarque_servicio(db, embarque)

@router.get("/", response_model=list[EmbarqueResponse])
def listar_embarques(db: Session = Depends(get_db)):
    return listar_embarques_servicio(db)