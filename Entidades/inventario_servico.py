from sqlalchemy.orm import Session
from Entidades.inventario import Inventario


def obtener_alertas_inventario(db: Session):
    Inventarios = db.query(Inventario).filter(
        Inventario.cantidad <= Inventario.stock_minimo
    ).all()

    resultado = []

    for item in Inventarios:
        resultado.append({
            "id": item.id,
            "product_id": item.product_id,
            "cantidad": item.cantidad,
            "ubicacion": item.ubicacion,
            "stock_minimo": item.stock_minimo
        })

        return resultado