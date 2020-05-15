conf = {
    "host": "localhost",
    "user": "martina",
    "passwd": "",
    "database": "ecommerce_final"
}

queries = {
    "listar_usuarios":"SELECT dni, nombre, apellido, email, clave, telefono, direccion_id, usuario_id FROM usuarios",
    "listar_productos":"SELECT nombre, descripcion, precio, categoria_id, marca_id, producto_id FROM productos",
    "listar_compras":"SELECT usuario_id, direccion_id, producto_id, cantidad, precio_total, compra_id FROM compras",
    "actualizar_producto_nombre":"UPDATE productos SET nombre = %s WHERE producto_id = %s",
    "actualizar_producto_descripcion":"UPDATE productos SET descripcion = %s WHERE producto_id = %s",
    "actualizar_producto_precio":"UPDATE productos SET precio = %s WHERE producto_id = %s",
    "actualizar_usuario_email":"UPDATE usuarios SET email = %s WHERE usuario_id = %s",
    "actualizar_usuario_clave":"UPDATE usuarios SET clave = %s WHERE usuario_id = %s",
    "actualizar_usuario_telefono":"UPDATE usuarios SET telefono = %s WHERE usuario_id = %s",
    "actualizar_usuario_direccion":"UPDATE usuarios SET direccion_id = %s WHERE usuario_id = %s",
    "agregar_producto":"INSERT INTO productos(nombre, descripcion, precio, categoria_id, marca_id) VALUES (%s, %s, %s, %s, %s)",
    "agregar_usuario":"INSERT INTO usuarios(dni, nombre, apellido, clave, email, telefono) VALUES (%s, %s, %s, %s)",
    "traer_usuario":"SELECT * FROM usuarios WHERE usuario_id = %s",
    "login_usuario":"SELECT clave, usuario_id FROM usuarios WHERE email = %s",
    "eliminar_producto":"DELETE FROM productos WHERE producto_id = %s",
    "eliminar_usuario":"DELETE FROM usuarios WHERE usuario_id = %s",
    "registrar_compra":"INSERT INTO compras(usuario_id, direccion_id, producto_id, cantidad, precio_total) VALUES (%s, %s, %s, %s, %s)"
}
