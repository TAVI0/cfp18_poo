class Compra:
    def __init__(self, usuario_id, direccion_id, producto_id, cantidad, precio_total, ID = 0):
        self.set_usuario_id(usuario_id)
        self.set_direccion_id(direccion_id)
        self.set_producto_id(producto_id)
        self.set_cantidad(cantidad)
        self.set_precio_total(precio_total)

    def get_usuario_id(self):
        return self.usuario_id

    def get_direccion_id(self):
        return self.direcicon_id

    def get_producto_id(self):
        return self.producto_id

    def get_cantidad(self):
        return self.cantidad

    def get_precio_total(self):
        return precio_total

    def set_usuario_id(self, usuario_id):
        self.usuario_id = usuario_id

    def set_direccion_id(self, direccion_id):
        self.direccion_id = direccion_id

    def set_producto_id(self, producto_id):
        self.producto_id(producto_id)

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio_total(self, precio_total):
        self.precio_total

    def set_compra_id(self, ID):
        self.id = ID
