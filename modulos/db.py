import mysql.connector
from dbconf import conf, queries
from usuarios import Usuario, crear_usuario_nuevo
from productos import Producto
from compras import Compra

class Ecommerce:
    def __init__(self, conf):
        self.conexion = mysql.connector.connect(**conf)
        self.cursor = self.conexion.cursor()

    def listar_usuarios(self):
        self.cursor.execute(queries["listar_usuarios"])
        resultados = self.cursor.fetchall()
        return resultados

    def traer_usuario(self, usuario_id):
        val = (usuario_id,)
        self.cursor.execute(queries["traer_usuario"], val)
        return self.cursor.fetchone()

    def login_usuario(self, email, clave):
        val = (email,)
        self.cursor.execute(queries["login_usuario"], val)
        return self.cursor.fetchone()

    def crear_usuario(self, usuario):
        val = (usuario.get_nombre(), usuario.get_apellido(), usuario.get_email(), usuario.get_clave(), usuario.get_telefono(), usuario.get_direccion_id())
        self.cursor.execute(queries["agregar_usuario"], val)
        self.conexion.commit()
        usuario.set_usuario_id(self.cursor.lastrowid)

    def crear_producto(self, producto):
        val = (producto.get_nombre(), producto.get_descripcion(), producto.get_precio(), producto.get_categoria_id(), producto.get_marca_id())
        self.cursor.execute(queries["agregar_producto"], val)
        self.conexion.commit()
        producto.set_producto_id(self.cursor.lastrowid)

    def crear_compra(self, compra):
        val = (compra.get_usuario_id(), compra.get_direccion_id(), compra.get_producto_id(), compra.get_cantidad(), compra.get_precio_total())
        self.cursor.execute(queries["registrar_compra"], val)
        self.conexion.commit()
        compra.set_compra_id(self.cursor.lastrowid)

    def eliminar_usuario(self, usuario):
        val = (usuario.get_id(),)
        self.cursor.execute(queries["eliminar_usuario"], val)
        self.conexion.commit()

    def eliminar_producto(self, usuario):
        val = (producto.get_id(),)
        self.cursor.execute(queries["eliminar_producto"], val)
        self.conexion.commit()

    def eliminar_compra(self, usuario):
        val = (compra.get_id(),)
        self.cursor.execute(queries["eliminar_compra"], val)
        self.conexion.commit()
