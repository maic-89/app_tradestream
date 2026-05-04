from Entidades.proveedor_repositorio import crear_proveedor, listar_proveedores

def crear_proveedor_servicio(db, proveedor):
    return crear_proveedor(db, proveedor)

def listar_proveedores_servicio(db):
    return listar_proveedores(db)