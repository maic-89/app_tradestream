from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
import os
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
from usuario_router import router as usuario_router


app = FastAPI()


app.include_router(core_router, prefix="/api/v1")  # Agrega el prefijo "/api/v1" a todas las rutas del core_router
app.include_router(pedido_router, prefix="/api/v1")
app.include_router(salida_router, prefix="/api/v1")
app.include_router(proveedor_router, prefix="/api/v1")
app.include_router(embarque_router, prefix="/api/v1")
app.include_router(recepcion_router, prefix="/api/v1")
app.include_router(kardex_router, prefix="/api/v1")
app.include_router(inventario_router, prefix="/api/v1")
app.include_router(usuario_router, prefix="/api/v1")
@app.get("/", tags=["Root"])
def inicio():
    return {
        "app": "TradeStream",
        "version": "1.0.0",
        "message": "SISTEMA DE COMPRAS INTERNACIONALES"
    }

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/registro", response_class=HTMLResponse)
def leer_registro():
    with open(os.path.join("static", "registro.html"), encoding="utf-8") as f:
        return f.read()
    
@app.get("/login", response_class=HTMLResponse)
def leer_login():
    with open(os.path.join("static", "login.html"), encoding="utf-8") as f:
        return f.read()
    
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print("Error de validación")
    print(exc.errors())
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )


# --- RUTAS DE NAVEGACIÓN DE INTERFAZ (HTML ENDPOINTS) ---

@app.get("/dashboard", response_class=HTMLResponse)
def leer_dashboard():
    with open(os.path.join("static", "dashboard.html"), encoding="utf-8") as f:
        return f.read()

@app.get("/pedidos", response_class=HTMLResponse)
def leer_pedidos():
    with open(os.path.join("static", "pedidos.html"), encoding="utf-8") as f:
        return f.read()

@app.get("/embarques", response_class=HTMLResponse)
def leer_embarques():
    with open(os.path.join("static", "embarques.html"), encoding="utf-8") as f:
        return f.read()

@app.get("/productos", response_class=HTMLResponse)
def leer_productos():
    with open(os.path.join("static", "productos.html"), encoding="utf-8") as f:
        return f.read()

@app.get("/inventario", response_class=HTMLResponse)
def leer_inventario():
    with open(os.path.join("static", "inventario.html"), encoding="utf-8") as f:
        return f.read()

@app.get("/kardex", response_class=HTMLResponse)
def leer_kardex():
    with open(os.path.join("static", "kardex.html"), encoding="utf-8") as f:
        return f.read()

@app.get("/proveedores", response_class=HTMLResponse)
def leer_proveedores():
    with open(os.path.join("static", "proveedores.html"), encoding="utf-8") as f:
        return f.read()

@app.get("/recepcion", response_class=HTMLResponse)
def leer_recepcion():
    with open(os.path.join("static", "recepcion.html"), encoding="utf-8") as f:
        return f.read()
    
@app.get("/usuario_db", response_class=HTMLResponse)
def leer_usuario_db():
    with open(os.path.join("static", "usuario_db.html"), encoding="utf-8") as f:
        return f.read()