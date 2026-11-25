class Pedido:
    def __init__(self, id_pedido, cliente):
        self._id_pedido = id_pedido
        self._cliente = cliente
        self._estado_pedido = EstadoPedido.REGISTRADO
        self._items = []        
        self._pago = None

    @property
    def id_pedido(self):
        return self._id_pedido

    @property
    def cliente(self):
        return self._cliente

    @property
    def estado_pedido(self):
        return self._estado_pedido

    @property
    def items(self):
        return list(self._items)  

    @property
    def pago(self):
        return self._pago
    def agregar_producto(self, producto, cantidad=1):
        
        if self._estado_pedido != EstadoPedido.REGISTRADO:
            raise ValueError("Solo se pueden agregar productos en estado REGISTRADO")
        
        if cantidad < 1 or cantidad > 20:
            raise ValueError("La cantidad debe estar entre 1 y 20")
        for i in range(cantidad):
            self._items.append(producto)
    def quitar_producto(self, producto):
        if self._estado_pedido != EstadoPedido.REGISTRADO:
            raise ValueError("Solo se pueden quitar productos en estado REGISTRADO")
        if producto not in self._items:
            raise ValueError("Ese producto no esta en el pedido")
        self._items.remove(producto)
    def cambiar_estado(self, nuevo_estado):
        actual = self._estado_pedido
        permitido = False
        if actual == EstadoPedido.REGISTRADO and nuevo_estado == EstadoPedido.EN_PREPARACION:
            permitido = True
        elif actual == EstadoPedido.REGISTRADO and nuevo_estado == EstadoPedido.CANCELADO:
            permitido = True
        elif actual == EstadoPedido.EN_PREPARACION and nuevo_estado == EstadoPedido.LISTO:
            permitido = True
        elif actual == EstadoPedido.LISTO and nuevo_estado == EstadoPedido.ENTREGADO:
            permitido = True
        if not permitido:
            raise ValueError("No se puede pasar de " + actual + " a " + nuevo_estado)
        self._estado_pedido = nuevo_estado
    def cancelar(self):
        self.cambiar_estado(EstadoPedido.CANCELADO)
    def calcular_cargos(self, subtotal):
        return 0
    def calcular_total(self):
        subtotal = 0
        for producto in self._items:
            subtotal = subtotal + producto.calcular_precio()
        return round(subtotal + self.calcular_cargos(subtotal), 2)
    def pagar(self, metodo_pago):
        if self._estado_pedido == EstadoPedido.CANCELADO:
            raise ValueError("No se puede cobrar un pedido cancelado")
        if self._pago != None:
            raise ValueError("El pedido ya fue pagado")
        metodo_pago.procesar_pago(self.calcular_total())
        self._pago = metodo_pago
        
class PedidoLocal(Pedido):
    def __init__(self, id_pedido, cliente, nro_mesa):
        super().__init__(id_pedido, cliente)
        if nro_mesa < 1 or nro_mesa > 15:
            raise ValueError("La mesa debe estar entre 1 y 15")
        self.__nro_mesa = nro_mesa
    @property
    def nro_mesa(self):
        return self.__nro_mesa
    def calcular_cargos(self, subtotal):
        return 0    
class PedidoLlevar(Pedido):
    def __init__(self, id_pedido, cliente):
        super().__init__(id_pedido, cliente)
        self.__costo_envase = 1.50    
    def calcular_cargos(self, subtotal):
        return round(len(self._items) * self.__costo_envase, 2)
class PedidoDelivery(Pedido):
    zonas = ["Cercado", "Quillacollo", "Sacaba", "Vinto"]
    tarifas = [8, 15, 15, 20]
    minimo_envio = 200       
    minutos_retraso = 0      
    def __init__(self, id_pedido, cliente, zona):
        super().__init__(id_pedido, cliente)
        if zona not in PedidoDelivery.zonas:
            raise ValueError("Zona no valida. Zonas: Cercado, Quillacollo, Sacaba, Vinto")
        self.__zona = zona
        self.__pedido_minimo = 35   

    @property
    def zona(self):
        return self.__zona
    def calcular_cargos(self, subtotal):
        if self.__zona == "Cercado" and subtotal >= PedidoDelivery.minimo_envio:
            return 0
        posicion = PedidoDelivery.zonas.index(self.__zona)
        return PedidoDelivery.tarifas[posicion]
    def calcular_retraso(self, minutos_entrega):
        if PedidoDelivery.minutos_retraso == 0:
            return False
        return minutos_entrega > PedidoDelivery.minutos_retraso
    def pagar(self, metodo_pago):
        subtotal = 0
        for producto in self._items:
            subtotal = subtotal + producto.calcular_precio()
        if subtotal < self.__pedido_minimo:
            raise ValueError("El pedido minimo para delivery es Bs " + str(self.__pedido_minimo))
        if not metodo_pago.permite_delivery:
            raise ValueError("El delivery solo acepta efectivo o QR")
        super().pagar(metodo_pago)
class EstadoPedido:
    REGISTRADO = "REGISTRADO"
    EN_PREPARACION = "EN_PREPARACION"
    LISTO = "LISTO"
    ENTREGADO = "ENTREGADO"
    CANCELADO = "CANCELADO"