from sqlalchemy.orm import Session
from Entidades.pedido import Pedido

def crear_pedido(db: Session, pedido: Pedido):
    total = pedido.cantidad * pedido.precio_unitario

    nuevo_pedido = Pedido(
        proveedor=pedido.proveedor,
        producto=pedido.producto,
        cantidad=pedido.cantidad,
        precio_unitario=pedido.precio_unitario,
        precio_total=total,

    )
    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)

    return nuevo_pedido

def listar_pedidos(db: Session):
    return db.query(Pedido).all()
