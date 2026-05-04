from requests import Session
from Entidades.pedido import Pedido
from Entidades.detalle_pedido_repositorio import crear_detalle_pedido


def listar_pedidos_servicio(db: Session):
    return db.query(Pedido).all()

def crear_pedido_servicio(db: Session, pedido_data):
    nuevo_pedido = Pedido(
        proveedor_id=pedido_data.proveedor_id,
        usuario_id=pedido_data.usuario_id,
        bodega_destino=pedido_data.bodega_destino,
        precio_total=0,
        )
   
    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)

    total = 0

    for item in pedido_data.detalles:
        detalle = crear_detalle_pedido(db, item, nuevo_pedido.id)
        total += detalle.subtotal

    nuevo_pedido.precio_total = total
    db.commit()
    db.refresh(nuevo_pedido)

    return nuevo_pedido