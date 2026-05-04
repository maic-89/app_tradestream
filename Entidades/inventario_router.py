from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from Entidades.inventario import Inventario
from Entidades.inventario_servico import obtener_alertas_inventario
from Entidades.inventario_schema import (InventarioResponse, InventarioAlertasResponse)
from Entidades.kardex import Kardex
from Entidades.kardex_schema import kardexResponse
from security import obtener_usuario_actual



router = APIRouter(prefix="/inventario", tags=["Inventario"]) 

@router.get("/", response_model=list[InventarioResponse])
def obtener_inventario(
    db: Session = Depends(get_db),
    user = Depends(obtener_usuario_actual)
):
    return db.query(Inventario).all()

@router.get("/movimientos-recientes", response_model=list[kardexResponse])
def movimientos_recientes(
    db: Session = Depends(get_db),
    user = Depends(obtener_usuario_actual)
    ):
        if user["rol"] not in ["ADMIN", "BODEGA"]:
             raise HTTPException(status_code=403, detail="No autorizado")
    
        return db.query(Kardex).order_by(Kardex.fecha.desc()).limit(10).all()


@router.get("/alertas", response_model=list[InventarioAlertasResponse])
def alertas_inventario(
    db: Session = Depends(get_db),
    user = Depends(obtener_usuario_actual)
):
    return obtener_alertas_inventario(db)