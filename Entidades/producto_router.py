from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from Entidades.producto_schema import ProductoCreate, ProductoResponse
from Entidades.producto_servicio import crear_producto_servicio, listar_productos_servicio

router  = APIRouter(prefix="/productos", tags=["productos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductoResponse)
def crear_producto_endpoint(producto: ProductoCreate, db: Session = Depends(get_db)):
    return crear_producto_servicio(db, producto)

@router.get("/", response_model=list[ProductoResponse])
def listar_productos_endpoint(db: Session = Depends(get_db)):
    return listar_productos_servicio(db)