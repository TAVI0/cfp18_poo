class Direccion:
    def __init__(self, calle, altura, codigo_postal, ciudad_id, ID = 0):
        self.set_calle(calle)
        self.set_altura(altura)
        self.set_codigo_postal(codigo_postal)
        self.set_ciudad_id(ciudad_id)
        self.set_direccion_id(ID)

    def get_calle(self):
        return self.calle

    def get_altura(self):
        return self.altura

    def get_codigo_postal(self):
        return self.codigo_posta

    def get_ciudad_id(self):
        return self.ciudad_id

    def get_direccion_id(self):
        return self.direccion_id

    def set_calle(self, calle):
        self.calle = calle

    def set_altura(self, altura):
        self.altura = altura

    def set_codigo_postal(self, codigo_postal):
        self.codigo_postal = codigo_postal

    def set_ciudad_id(self, ciudad_id):
        self.ciudad_id = ciudad_id

    def set_direccion_id(self, ID):
        self.direccion_id = ID
