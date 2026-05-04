from fastapi import FastAPI
from core_router import router as core_router
from Entidades.pedido_router import router as pedido_router
from Entidades.proveedor_router import router as proveedor_router
from Entidades.embarque_router import router as embarque_router
from Entidades.recepcion_router import router as recepcion_router
from Entidades.kardex_router import router as kardex_router 
from Entidades.salida_router import router as salida_router 
from Entidades.inventario_router import router as inventario_router
from usuario_db import Usuario 
from Entidades.producto import Producto
from Entidades.proveedor import Proveedor


app = FastAPI()
app.include_router(core_router, prefix="/api/v1")  # Agrega el prefijo "/api/v1" a todas las rutas del core_router
app.include_router(pedido_router, prefix="/api/v1")
app.include_router(salida_router, prefix="/api/v1")
app.include_router(proveedor_router, prefix="/api/v1")
app.include_router(embarque_router, prefix="/api/v1")
app.include_router(recepcion_router, prefix="/api/v1")
app.include_router(kardex_router, prefix="/api/v1")
app.include_router(inventario_router, prefix="/api/v1")

@app.get("/", tags=["Root"])
def inicio():
    return {
        "app": "TradeStream",
        "version": "1.0.0",
        "message": "SISTEMA DE COMPRAS INTERNACIONALES"
    }