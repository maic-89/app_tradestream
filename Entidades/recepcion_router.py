from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from Entidades.recepcion_completa_schema import RecepcionCompleta
from Entidades.recepcion_servicio import crear_recepcion_completa
from security import obtener_usuario_actual

router = APIRouter(prefix="/recepciones", tags=["recepciones"])

@router.post("/")
def crear_recepcion_endpoint(
    data: RecepcionCompleta,
    db: Session = Depends(get_db),
    user = Depends(obtener_usuario_actual)
):
    return crear_recepcion_completa(db, data, user)