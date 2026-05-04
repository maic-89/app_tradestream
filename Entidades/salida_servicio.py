from Entidades.salida import Salida
from Entidades.detalle_salida import DetalleSalida
from Entidades.inventario import Inventario
from Entidades.kardex_servicio import registrar_movimiento
from fastapi import HTTPException

def crear_salida_completa(db, data):
    # Crear la salida
    salida = Salida(fecha=data.fecha)
    db.add(salida)
    db.commit()
    db.refresh(salida)

    for item in data.detalles:

        inventario = db.query(Inventario).filter(
            Inventario.producto_id == item.producto_id
            ).first()
        if not inventario or inventario.cantidad < item.cantidad:
            raise HTTPException(
                status_code=400, 
                detail=f"Inventario insuficiente para producto {item.producto_id}"
            )
        
        # Crear el detalle de salida

        stock_anterior = Inventario.cantidad
        Inventario.cantidad -= item.cantidad
        stock_actual = Inventario.cantidad
        

        detalle = DetalleSalida(
            salida_id=Salida.id,
            producto_id=item.producto_id,
            cantidad=item.cantidad)
        
        db.add(detalle)

        registrar_movimiento(
            db, 
            producto_id=item.producto_id, 
            cantidad=item.cantidad, 
            tipo_movimiento="salida", 
            stock_anterior=stock_anterior, 
            stock_actual=stock_actual,
            tipo_documento="SALIDA",
            costo_unitario=0,
            usuario=user["username"]

            )
        
    db.commit()
    return Salida