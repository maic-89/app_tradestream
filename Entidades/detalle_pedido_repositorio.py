from sqlalchemy.orm import Session
from Entidades.detalle_pedido import DetallePedido

def crear_detalle_pedido(db: Session, detalle_pedido):
    subtotal = detalle_pedido.cantidad * detalle_pedido.precio_unitario

    nuevo = DetallePedido(
        pedido_id=detalle_pedido.pedido_id,
        producto_id=detalle_pedido.producto_id,
        cantidad=detalle_pedido.cantidad,
        precio_unitario=detalle_pedido.precio_unitario,
        subtotal=subtotal
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo 