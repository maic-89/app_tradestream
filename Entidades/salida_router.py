from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from Entidades.salida_completa_schema import SalidaCompletaSchema
from Entidades.salida_servicio import crear_salida_completa
from security import obtener_usuario_actual

router = APIRouter(prefix="/salidas", tags=["salidas"])

@router.post("/")
def crear_salida_completa(
    data: SalidaCompletaSchema,
    db: Session = Depends(get_db),
    user = Depends(obtener_usuario_actual)
):
    
    if user["rol"] not in ["ADMIN","BODEGA"]:
        raise HTTPException(status_code=403, detail="No autorizado")

    return crear_salida_completa(db, data)