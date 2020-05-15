import base64

class Usuario:
    def __init__(self, dni, nombre, apellido, email, clave, telefono, direccion_id = 0, ID = 0):
        self.set_dni(dni)
        self.set_nombre(nombre)
        self.set_apellido(apellido)
        self.set_email(email)
        self.set_clave(clave)
        self.set_telefono(telefono)
        self.set_direccion_id(direccion_id)
        self.set_usuario_id(ID)

    def get_dni(self):
        return self.dni

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_email(self):
        return self.email

    def get_clave(self):
        return base64.encodebytes(self.clave.encode())

    def get_telefono(self):
        return self.telefono

    def get_direccion_id(self):
        return self.direccion_id

    def get_usuario_id(self):
        return self.id

    def set_dni(self, dni):
        try:
            dni = int(dni)
        except:
            dni = None
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre.capitalize()

    def set_apellido(self, apellido):
        self.apellido = apellido.capitalize()

    def set_email(self, email):
        self.email = email

    def set_clave(self, clave):
        self.clave = clave

    def set_telefono(self, telefono):
        try:
            telefono = int(telefono)
        except:
            telefono = None
        self.telefono = telefono

    def set_direccion_id(self, direccion_id):
        self.direccion_id = int(direccion_id)

    def set_usuario_id(self, ID):
        self.id = int(ID)

def crear_usuario_nuevo(email):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = int(input("DNI: "))
    clave = input("Clave: ")
    telefono = int(input("Telefono: "))
    return Usuario(dni, nombre, apellido, email, clave, telefono)
