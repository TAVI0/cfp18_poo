from db import *

db = Ecommerce(conf)

usuarios = db.listar_usuarios()

for datos in usuarios:
    # ~ print(datos)
    dni, nombre, apellido, email, clave, telefono, direccion_id, usuario_id = datos
    usuario = Usuario(dni, nombre, apellido, email, clave, telefono, 0, usuario_id)
    print(usuario.get_usuario_id(), usuario.get_clave(), usuario.clave)
