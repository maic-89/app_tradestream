from sqlalchemy.orm import Session 
from Entidades.producto import Producto

def crear_producto(db:  Session, producto):
    nuevo = Producto(**producto.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_productos(db: Session):
    return db.query(Producto).all()
