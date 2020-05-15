class Producto:
    def __init__(self, nombre, descripcion, precio, categoria_id, marca_id, ID = 0):
        self.set_nombre(nombre)
        self.set_descripcion(descripcion)
        self.set_precio(precio)
        self.set_categoria_id(categoria_id)
        self.set_marca_id(marca_id)

    def get_nombre(self):
        return self.nombre

    def get_descripcion(self):
        return self.descripcion

    def get_precio(self):
        return self.precio

    def get_categoria_id(self):
        return self.categoria_id

    def get_marca_id(self):
        return self.marca_id

    def get_producto_id(self):
        return self.id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def set_precio(self, precio):
        try:
            precio = float(precio)
        except:
            precio = None
        self.precio = precio

    def set_marca_id(self, marca_id):
        self.marca_id = marca_id

    def set_categoria_id(self, categoria_id):
        self.categoria_id = categoria_id

    def set_producto_id(self, ID):
        self.id = ID
