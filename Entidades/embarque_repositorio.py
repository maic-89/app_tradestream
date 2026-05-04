from sqlalchemy.orm import Session
from Entidades.embarque import Embarque

def crear_embarque_servicio(db: Session, embarque: Embarque):
    nuevo = Embarque(**embarque.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_embarques_servicio(db: Session):
    return db.query(Embarque).all()