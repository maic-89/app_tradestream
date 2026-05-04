from datetime import date
from fastapi import APIRouter, Depends, Query
from fastapi.responses import StreamingResponse
from Entidades.kardex_servicio import generar_excel_kardex
from sqlalchemy.orm import Session

from database import get_db
from Entidades.kardex import Kardex
from Entidades.kardex_schema import kardexResponse
from security import obtener_usuario_actual

router = APIRouter(prefix="/kardex", tags=["Kardex"])

@router.get("/", response_model=list[kardexResponse])
def listar_kardex(
    db: Session = Depends(get_db),
    user = Depends(obtener_usuario_actual)
    ):
    
    return db.query(Kardex).all()

@router.get("/producto/{product_id}", response_model=list[kardexResponse])
def kardex_por_producto(
    product_id: int,
    fecha_inicio: date | None = Query(None),
    fecha_fin: date | None = Query(None),
    db: Session = Depends(get_db),
    user = Depends(obtener_usuario_actual)
    
):
    
    query = db.query(Kardex).filter(Kardex.producto_id == product_id)

    if fecha_inicio:
        query = query.filter(Kardex.fecha_movimiento >= fecha_inicio)
    
    if fecha_fin:
        query = query.filter(Kardex.fecha_movimiento <= fecha_fin)

    return query.all()
    
@router.get("/producto/{product_id}/exportar")
def exportar_kardex_excel(
    product_id: int,
    fecha_inicio: date | None = Query(None),
    fecha_fin: date | None = Query(None),
    db: Session = Depends(get_db),
    user = Depends(obtener_usuario_actual)
):
    query = db.query(Kardex).filter(Kardex.producto_id == product_id)
    if fecha_inicio:
        query = query.filter(Kardex.fecha_movimiento >= fecha_inicio)

    if fecha_fin:
        query = query.filter(Kardex.fecha_movimiento <= fecha_fin)

    movimientos = query.order_by(Kardex.fecha_movimiento.asc()).all()

    excel_file = generar_excel_kardex(movimientos)

    return StreamingResponse(
        excel_file,
        media_type="application/vnd.openxmlformats-officedocument.epreasheetml.sheet",
        headers={
            "Content-Disposition": f"attachment; filename=kardex_producto_{product_id}.xlsx"
        }
    )

