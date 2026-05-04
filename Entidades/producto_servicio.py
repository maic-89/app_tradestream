from Entidades.producto_repositorio import listar_productos, crear_producto

def crear_producto_servicio(db, producto):
    return crear_producto(db, producto)

def listar_productos_servicio(db):
    return listar_productos(db)