from Entidades.kardex import Kardex
from openpyxl import Workbook
from io import BytesIO

def registrar_movimiento(
    db,
    product_id,
    tipo_movimiento,
    cantidad,
    stock_anterior,
    stock_actual,
    referencia,
    documento_id,
    costo_unitario: float= 0,
    usuario=None
):
    
    ultimo = db.query(Kardex).filter(
        Kardex.producto_id == product_id
        ).order_by(Kardex.fecha_movimiento.desc()).first()
    
    saldo_anterior = ultimo.saldo_valorizado if ultimo else 0

    if tipo_movimiento == "entrada":
       saldo_nuevo = saldo_anterior +(cantidad * costo_unitario)
    else:
        saldo_nuevo = saldo_anterior - (cantidad * costo_unitario)

    nuevo_movimiento = Kardex(
        product_id=product_id,
        tipo_movimiento=tipo_movimiento,
        cantidad=cantidad,
        stock_anterior=stock_anterior,
        stock_actual=stock_actual,
        referencia=referencia,
        documento_id=documento_id,
        costo_unitario=costo_unitario,
        saldo_valorizado = saldo_nuevo,
        usuario = usuario

    )
    db.add(nuevo_movimiento)

def generar_excel_kardex(movimientos):
    wb = Workbook()
    ws = wb.active
    ws.tittle = "Kardex"

    headers = [
       "Fecha Movimiento", 
       "Tipo Movimiento",
       "Tipo Documento",
       "Stock Anterior",
       "Stock Actual",
       "Costo Unitario",
       "Producto ID", 
       "Cantidad",
       "usuario"

    ]
    ws.append(headers)
    #Datos de ejemplo, reemplaza con tus datos reales
    data = []
    for mov in movimientos:
        ws.append({
            mov.fecha_movimiento,
            mov.tipo_movimiento,
            mov.tipo_documento,
            mov.stock_anterior,
            mov.stock_actual,
            mov.costo_unitario,
            mov.producto_id,
            mov.cantidad,
            mov.usuario

        })

    Stream = BytesIO()
    wb.save(Stream)
    Stream.seek(0)

    return Stream