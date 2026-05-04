from Entidades.recepcion import Recepcion
from Entidades.detalle_recepcion import DetalleRecepcion
from Entidades.inventario import Inventario
from Entidades.kardex_servicio import registrar_movimiento

def crear_recepcion_completa(db, data):
    # Crear la recepción
    try:    

        recepcion = Recepcion(
            fecha=data.fecha_recepcion, 
            proveedor_id=data.proveedor_id
            )
        
        db.add(recepcion)
        db.flush()  # Asegura que recepcion.id esté disponible


        # Crear los detalles de la recepción
        for item in data.detalles:

            inventario = db.query(Inventario).filter(
                Inventario.producto_id == item.producto_id
            ).first()
            
            if not inventario:
                inventario = Inventario(
                    producto_id=item.producto_id,
                    cantidad=0
                )

                db.add(inventario)
                db.flush()  # Asegura que inventario.id esté disponible
    
            stock_anterior = inventario.cantidad
            inventario.cantidad += item.cantidad
            stock_actual = inventario.cantidad

            detalle = DetalleRecepcion(
                recepcion_id=recepcion.id,
                producto_id=item.producto_id,
                cantidad=item.cantidad,
                costo_unitario=item.costo_unitario
            )

            db.add(detalle)
            
            registrar_movimiento(
                db,
                id_producto=item.producto_id,
                tipo_movimiento='recepcion',
                cantidad=item.cantidad,
                stock_anterior=stock_anterior,
                stock_actual=stock_actual,
                tipo_documento='recepcion',
                documento_id=recepcion.id,
                costo_unitario=item.costo_unitario
            )

        db.commit()
        return recepcion

    except Exception as e:
        db.rollback()
        raise e