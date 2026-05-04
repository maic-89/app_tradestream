from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Entidades.pedido import Pedido
from database import SessionLocal
from Entidades.pedido_schema import PedidoCreate, PedidoResponse
from Entidades.pedido_servicio import crear_pedido_servicio, listar_pedidos_servicio


router = APIRouter(prefix="/pedidos", tags=["pedidos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/completo")
def crear_pedido_completo_endpoint(pedido: PedidoCreate, db: Session = Depends(get_db)):
    return crear_pedido_servicio(db, pedido)

@router.get("/", response_model=list[PedidoResponse])
def listar_pedidos_endpoint(db: Session = Depends(get_db)):
    return listar_pedidos_servicio(db)

    