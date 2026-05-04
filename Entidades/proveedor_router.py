from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from Entidades.proveedor_schema import ProveedorCreate, ProveedorResponse
from Entidades.proveedor_servicio import crear_proveedor_servicio, listar_proveedores_servicio

router  = APIRouter(prefix="/proveedores", tags=["proveedores"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProveedorResponse)
def crear_proveedor_endpoint(proveedor: ProveedorCreate, db: Session = Depends(get_db)):
    return crear_proveedor_servicio(db, proveedor)

@router.get("/", response_model=list[ProveedorResponse])
def listar_proveedores_endpoint(db: Session = Depends(get_db)):
    return listar_proveedores_servicio(db)

