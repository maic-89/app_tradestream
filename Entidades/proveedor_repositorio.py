from sqlalchemy.orm import Session
from Entidades.proveedor import Proveedor

def crear_proveedor(db: Session, proveedor):
    nuevo = Proveedor(**proveedor.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_proveedores(db: Session):
    return db.query(Proveedor).all()