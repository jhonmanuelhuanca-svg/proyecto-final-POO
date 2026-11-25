class Cliente:
    def __init__(self, nombre, telefono, direccion):
        if not self.validar_telefono(telefono):
            raise ValueError("El telefono debe tener 8 digitos y empezar con 6 o 7")
        self.__nombre = nombre
        self.__telefono = telefono
        self.__direccion = direccion
    @property
    def nombre(self):
        return self.__nombre
    @property
    def telefono(self):
        return self.__telefono
    @property
    def direccion(self):
        return self.__direccion
    def validar_telefono(self, telefono):
        if len(telefono) != 8 or not telefono.isdigit():
            return False
        return telefono[0] == "6" or telefono[0] == "7"