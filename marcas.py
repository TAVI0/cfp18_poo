class Marca:
    def __init__(self,marca_id,nombre):
        self.set_nombre(nombre)
        self.set_marca_id(marca_id)

    def get_marca_id(self):
        return self.marca_id

    def get_nombre(self):
        return self.nombre

    def set_marca_id(self, marca_id):
        self.marca_id = marca_id
    
    def set_nombre(self, nombre):
        self.nombre = nombre

