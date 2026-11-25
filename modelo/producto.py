class Producto:

    def __init__(self, id_producto, nombre):
        self._id_producto = id_producto
        self._nombre = nombre

    @property
    def id_producto(self):
        return self._id_producto

    @property
    def nombre(self):
        return self._nombre

    def calcular_precio(self):
        return 0

    def esta_disponible(self, dia):
        return True

class Plato(Producto):

    def __init__(self, id_producto, nombre, precio, dias_venta):
        super().__init__(id_producto, nombre)
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        self.__precio = precio
        self.__dias_venta = dias_venta

    def esta_disponible(self, dia):
        return dia in self.__dias_venta
    def calcular_precio(self):
        return self.__precio
class Bebida(Producto):
    def __init__(self, id_producto, nombre, tipo, precio_vaso, es_jarra):
        super().__init__(id_producto, nombre)
        if precio_vaso <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        self.__tipo = tipo
        self.__precio_vaso = precio_vaso
        self.__precio_jarra = precio_vaso * 3   
        self.__es_jarra = es_jarra
    def calcular_precio(self):
        if self.__es_jarra:
            return self.__precio_jarra
        return self.__precio_vaso
    
class Combo(Producto):
    descuento = 0.08       
    MAX_PRODUCTOS = 4       
    def __init__(self, id_producto, nombre):
        super().__init__(id_producto, nombre)
        self.__producto = []    

    @property
    def producto(self):
        return list(self.__producto)
    def validar_producto(self, producto, cantidad):
        if producto == self:
            raise ValueError("Un combo no puede contenerse a si mismo")
        total = cantidad
        for combo_producto in self.__producto:
            total = total + combo_producto.contar_total()
        if cantidad < 1 or total > Combo.MAX_PRODUCTOS:
            raise ValueError("Un combo tiene de 2 a 4 productos")
    def agregar_producto(self, producto, cantidad=1):
        self.validar_producto(producto, cantidad)
        self.__producto.append(ComboProducto(producto, cantidad, self))
    def quitar_producto(self, producto):
        for combo_producto in self.__producto:
            if combo_producto.producto == producto:
                self.__producto.remove(combo_producto)
                return
        raise ValueError("Ese producto no esta en el combo")
    def calcular_precio(self):
        suma = 0
        for combo_producto in self.__producto:
            suma = suma + combo_producto.calcular_total()
        return round(suma * (1 - Combo.descuento), 2)
    def esta_disponible(self, dia):
        for combo_producto in self.__producto:
            if not combo_producto.producto.esta_disponible(dia):
                return False
        return True

class ComboProducto:
    def __init__(self, producto, cantidad, combo):
        self.__producto = producto
        self.__cantidad = cantidad
        self.__combo = combo

    @property
    def producto(self):
        return self.__producto
    def calcular_total(self):
        return self.__producto.calcular_precio() * self.__cantidad
    def contar_total(self):
        return self.__cantidad