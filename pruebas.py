from modelo.pedido import EstadoPedido, Pedido, PedidoLocal, PedidoLlevar, PedidoDelivery
from modelo.cliente import Cliente
from modelo.producto import Producto, Plato, Bebida, Combo
from modelo.pagos import MetodoPago, PagoEfectivo, PagoQR, PagoTarjeta

class Pruebas:

    def __init__(self):
        dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        self.cliente = Cliente("Ana", "71234567", "Calle Jordan")
        self.silpancho = Plato(1, "Silpancho", 35, dias)
        self.pique = Plato(2, "Pique macho", 50, dias)
        self.mocochinchi = Bebida(3, "Mocochinchi", "natural", 6, False)
        self.combo_a = Combo(10, "Combo A")
        self.combo_a.agregar_producto(self.silpancho, 1)
        self.combo_a.agregar_producto(self.mocochinchi, 1)
        self.aprobadas = 0
    def ok(self, mensaje):
        self.aprobadas = self.aprobadas + 1
        print("OK - " + mensaje)
    def prueba_1(self):
        assert self.combo_a.calcular_precio() == 37.72
        self.ok("combo de referencia = Bs 37.72")
    def prueba_2(self):
        combo_b = Combo(11, "Combo B")
        combo_b.agregar_producto(self.combo_a, 1)
        combo_b.agregar_producto(self.pique, 1)
        assert combo_b.calcular_precio() == 80.70
        self.ok("combo que contiene otro combo = Bs 80.70")
    def prueba_3(self):
        pedido = PedidoDelivery(1, self.cliente, "Quillacollo")
        pedido.agregar_producto(self.combo_a, 2)
        assert pedido.calcular_total() == 90.44
        self.ok("2 combos por delivery a Quillacollo = Bs 90.44")
    def prueba_4(self):
        pedido = PedidoLlevar(2, self.cliente)
        pedido.agregar_producto(self.silpancho, 2)
        pedido.agregar_producto(self.mocochinchi, 1)
        assert pedido.calcular_total() == 80.50
        self.ok("para llevar: 76 + 3 envases x 1.50 = Bs 80.50")
    def prueba_5(self):
        jarra = Bebida(4, "Jarra", "natural", 6, True)
        assert jarra.calcular_precio() == 18
        self.ok("la jarra cuesta 3 vasos")
    def prueba_6(self):
        errores = 0
        try:
            Cliente("Luis", "51234567", "Av. Blanco Galindo")
        except ValueError:
            errores = errores + 1
        try:
            Plato(5, "Gratis", 0, ["lunes"])
        except ValueError:
            errores = errores + 1
        try:
            PedidoLocal(3, self.cliente, 5).agregar_producto(self.silpancho, 21)
        except ValueError:
            errores = errores + 1
        assert errores == 3
        self.ok("regla 8: telefono, precio y cantidad invalidos lanzan error")
    def prueba_7(self):
        pedido = PedidoLocal(4, self.cliente, 6)
        pedido.agregar_producto(self.silpancho)
        errores = 0
        try:
            pedido.cambiar_estado(EstadoPedido.LISTO)
        except ValueError:
            errores = errores + 1
        pedido.cambiar_estado(EstadoPedido.EN_PREPARACION)
        try:
            pedido.agregar_producto(self.pique)
        except ValueError:
            errores = errores + 1
        try:
            pedido.cancelar()
        except ValueError:
            errores = errores + 1
        assert errores == 3
        self.ok("regla 6: cambios de estado invalidos lanzan error")
    def prueba_8(self):
        pedido = PedidoDelivery(5, self.cliente, "Cercado")
        pedido.agregar_producto(self.pique)
        try:
            pedido.pagar(PagoTarjeta())
            assert False
        except ValueError:
            pass
        pedido.pagar(PagoQR("1234567890"))
        assert pedido.pago.monto_total == 58
        self.ok("el delivery rechaza tarjeta y acepta QR")
    def prueba_9(self):
        combo = Combo(12, "Combo grande")
        combo.agregar_producto(self.silpancho, 4)
        errores = 0
        try:
            combo.agregar_producto(self.mocochinchi, 1)
        except ValueError:
            errores = errores + 1
        try:
            combo.agregar_producto(combo, 1)
        except ValueError:
            errores = errores + 1
        assert errores == 2
        self.ok("combo con maximo 4 productos y sin contenerse a si mismo")
    def prueba_10(self):
        pedido = PedidoLocal(6, self.cliente, 7)
        pedido.agregar_producto(self.pique, 2)
        pago = PagoEfectivo(150)
        pedido.pagar(pago)
        assert pago.calcular_cambio() == 50
        pedido2 = PedidoLocal(7, self.cliente, 8)
        pedido2.agregar_producto(self.pique, 2)
        pedido2.pagar(PagoTarjeta())
        assert pedido2.pago.monto_total == 103
        self.ok("efectivo con cambio y tarjeta con 3 % de comision")
    def prueba_11(self):
        cercado = PedidoDelivery(8, self.cliente, "Cercado")
        cercado.agregar_producto(self.pique, 4)
        sacaba = PedidoDelivery(9, self.cliente, "Sacaba")
        sacaba.agregar_producto(self.pique, 4)
        assert cercado.calcular_total() == 200
        assert sacaba.calcular_total() == 215
        self.ok("envio gratis desde Bs 200 solo en Cercado")
    def prueba_12(self):
        pedido = PedidoDelivery(10, self.cliente, "Vinto")
        pedido.agregar_producto(self.mocochinchi)
        try:
            pedido.pagar(PagoEfectivo(100))
            assert False
        except ValueError:
            self.ok("pedido minimo de delivery Bs 35")
    def prueba_13(self):
        chicharron = Plato(13, "Chicharron", 45, ["domingo"])
        combo = Combo(14, "Combo domingo")
        combo.agregar_producto(chicharron, 1)
        combo.agregar_producto(self.mocochinchi, 1)
        assert combo.esta_disponible("domingo") == True
        assert combo.esta_disponible("lunes") == False
        assert self.mocochinchi.esta_disponible("lunes") == True
        self.ok("regla 4: disponibilidad por dia")
    def prueba_14(self):
        assert issubclass(Plato, Producto) and issubclass(Combo, Producto)
        assert issubclass(PedidoDelivery, Pedido) and issubclass(PagoTarjeta, MetodoPago)
        assert Producto(50, "Generico").calcular_precio() == 0
        assert self.silpancho.nombre == "Silpancho"
        assert self.silpancho.calcular_precio() == 35
        self.ok("herencia: super().__init__() y metodos sobrescritos")
    def ejecutar(self):
        self.prueba_1()
        self.prueba_2()
        self.prueba_3()
        self.prueba_4()
        self.prueba_5()
        self.prueba_6()
        self.prueba_7()
        self.prueba_8()
        self.prueba_9()
        self.prueba_10()
        self.prueba_11()
        self.prueba_12()
        self.prueba_13()
        self.prueba_14()
        print("Pruebas aprobadas: " + str(self.aprobadas))
pruebas = Pruebas()
pruebas.ejecutar()
