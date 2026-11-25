from modelo.pedido import EstadoPedido, PedidoLocal, PedidoLlevar, PedidoDelivery
from modelo.cliente import Cliente
from modelo.producto import Plato, Bebida, Combo
from modelo.pagos import PagoEfectivo, PagoQR, PagoTarjeta


class SistemaPedidos:

    def __init__(self, dia):
        self.dia = dia
        self.menu = []
        self.clientes = []
        self.pedidos = []
        self.cargar_menu()


    def cargar_menu(self):
        dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        silpancho = Plato(1, "Silpancho", 35, dias)
        pique = Plato(2, "Pique macho", 50, dias)
        chicharron = Plato(3, "Chicharron", 45, ["domingo"])
        sopa = Plato(4, "Sopa de mani", 20, dias)
        mocochinchi = Bebida(5, "Mocochinchi vaso", "natural", 6, False)
        jarra = Bebida(6, "Mocochinchi jarra", "natural", 6, True)
        gaseosa = Bebida(7, "Gaseosa vaso", "gaseosa", 8, False)
        combo = Combo(8, "Combo Valluno")
        combo.agregar_producto(silpancho, 1)
        combo.agregar_producto(mocochinchi, 1)
        self.menu = [silpancho, pique, chicharron, sopa, mocochinchi, jarra, gaseosa, combo]


    def buscar_producto(self, codigo):
        for producto in self.menu:
            if producto.id_producto == codigo:
                return producto
        raise ValueError("No existe el producto " + str(codigo))

    def buscar_cliente(self, telefono):
        for cliente in self.clientes:
            if cliente.telefono == telefono:
                return cliente
        raise ValueError("No existe un cliente con ese telefono. Registrelo primero (opcion 4)")

    def buscar_pedido(self, numero):
        for pedido in self.pedidos:
            if pedido.id_pedido == numero:
                return pedido
        raise ValueError("No existe el pedido " + str(numero))

   
    def mostrar_menu(self):
        print("--- Menu de hoy (" + self.dia + ") ---")
        for producto in self.menu:
            if producto.esta_disponible(self.dia):
                print(str(producto.id_producto) + ". " + producto.nombre + " - Bs " + str(producto.calcular_precio()))

    def registrar_producto(self):
        codigo = len(self.menu) + 1
        tipo = input("1 = Plato, 2 = Bebida: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        if tipo == "1":
            dias = input("Dias de venta (ej: lunes,martes): ").split(",")
            producto = Plato(codigo, nombre, precio, dias)
        else:
            es_jarra = input("Es jarra? (s/n): ") == "s"
            producto = Bebida(codigo, nombre, "natural", precio, es_jarra)
        self.menu.append(producto)
        print("Producto registrado: " + producto.nombre)

    def armar_combo(self):
        combo = Combo(len(self.menu) + 1, input("Nombre del combo: "))
        self.mostrar_menu()
        codigo = int(input("Codigo del producto (0 para terminar): "))
        while codigo != 0:
            cantidad = int(input("Cantidad: "))
            combo.agregar_producto(self.buscar_producto(codigo), cantidad)
            codigo = int(input("Codigo del producto (0 para terminar): "))
        total = 0
        for combo_producto in combo.producto:
            total = total + combo_producto.contar_total()
        if total >= 2:
            self.menu.append(combo)
            print("Combo registrado: " + combo.nombre + " - Bs " + str(combo.calcular_precio()))
        else:
            print("Un combo necesita al menos 2 productos")


    def registrar_cliente(self):
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        direccion = input("Direccion: ")
        cliente = Cliente(nombre, telefono, direccion)
        self.clientes.append(cliente)
        print("Cliente registrado: " + cliente.nombre)


    def nuevo_pedido(self):
        cliente = self.buscar_cliente(input("Telefono del cliente: "))
        numero = len(self.pedidos) + 1
        tipo = input("1 = Local, 2 = Para llevar, 3 = Delivery: ")
        if tipo == "1":
            mesa = int(input("Numero de mesa (1 a 15): "))

            for otro in self.pedidos:
                abierto = otro.estado_pedido != EstadoPedido.ENTREGADO and otro.estado_pedido != EstadoPedido.CANCELADO
                if isinstance(otro, PedidoLocal) and otro.nro_mesa == mesa and abierto:
                    raise ValueError("La mesa " + str(mesa) + " ya tiene un pedido abierto")
            pedido = PedidoLocal(numero, cliente, mesa)
        elif tipo == "2":
            pedido = PedidoLlevar(numero, cliente)
        else:
            zona = input("Zona (Cercado, Quillacollo, Sacaba, Vinto): ").capitalize()
            pedido = PedidoDelivery(numero, cliente, zona)
        self.pedidos.append(pedido)
        print("Pedido " + str(numero) + " creado para " + cliente.nombre)
        self.agregar_productos(pedido)

    def agregar_productos(self, pedido):
        self.mostrar_menu()
        codigo = int(input("Codigo del producto (0 para terminar): "))
        while codigo != 0:
            producto = self.buscar_producto(codigo)
            if producto.esta_disponible(self.dia):
                cantidad = int(input("Cantidad (1 a 20): "))
                pedido.agregar_producto(producto, cantidad)
                print("Total hasta ahora: Bs " + str(pedido.calcular_total()))
            else:
                print(producto.nombre + " no esta disponible hoy")
            codigo = int(input("Codigo del producto (0 para terminar): "))

    def quitar_producto(self):
        pedido = self.buscar_pedido(int(input("Numero de pedido: ")))
        producto = self.buscar_producto(int(input("Codigo del producto a quitar: ")))
        pedido.quitar_producto(producto)
        print("Producto quitado. Total: Bs " + str(pedido.calcular_total()))


    def ver_detalle(self):
        pedido = self.buscar_pedido(int(input("Numero de pedido: ")))
        print("--- Pedido " + str(pedido.id_pedido) + " (" + pedido.estado_pedido + ") ---")
        print("Cliente: " + pedido.cliente.nombre)
        subtotal = 0
        descuentos = 0
        mostrados = []
        for producto in pedido.items:
            subtotal = subtotal + producto.calcular_precio()
            if isinstance(producto, Combo):
                suma = 0
                for combo_producto in producto.producto:
                    suma = suma + combo_producto.calcular_total()
                descuentos = descuentos + suma * Combo.descuento
            if producto not in mostrados:
                mostrados.append(producto)
                cantidad = pedido.items.count(producto)
                print(str(cantidad) + " x " + producto.nombre + " - Bs " + str(round(producto.calcular_precio() * cantidad, 2)))
        print("Descuentos: Bs " + str(round(descuentos, 2)))
        print("Subtotal:   Bs " + str(round(subtotal, 2)))
        print("Cargos:     Bs " + str(pedido.calcular_cargos(subtotal)))
        print("TOTAL:      Bs " + str(pedido.calcular_total()))


    def cambiar_estado(self):
        pedido = self.buscar_pedido(int(input("Numero de pedido: ")))
        print("Estado actual: " + pedido.estado_pedido)
        opcion = input("1 = EN_PREPARACION, 2 = LISTO, 3 = ENTREGADO, 4 = CANCELADO: ")
        if opcion == "1":
            pedido.cambiar_estado(EstadoPedido.EN_PREPARACION)
        elif opcion == "2":
            pedido.cambiar_estado(EstadoPedido.LISTO)
        elif opcion == "3":
            pedido.cambiar_estado(EstadoPedido.ENTREGADO)
        elif opcion == "4":
            pedido.cancelar()
        print("Nuevo estado: " + pedido.estado_pedido)


    def cobrar(self):
        pedido = self.buscar_pedido(int(input("Numero de pedido: ")))
        print("Total a pagar: Bs " + str(pedido.calcular_total()))
        opcion = input("1 = Efectivo, 2 = QR, 3 = Tarjeta (+3%): ")
        if opcion == "1":
            pago = PagoEfectivo(float(input("Monto recibido: ")))
        elif opcion == "2":
            pago = PagoQR(input("Codigo de transaccion (10 digitos): "))
        else:
            pago = PagoTarjeta()
        pedido.pagar(pago)
        print("----- COMPROBANTE -----")
        print("Pedido " + str(pedido.id_pedido) + " - Cliente: " + pedido.cliente.nombre)
        print("Total pagado: Bs " + str(pago.monto_total))
        if opcion == "1":
            print("Cambio: Bs " + str(pago.calcular_cambio()))


    def reporte(self):
        local = 0
        llevar = 0
        delivery = 0
        nombres = []
        cantidades = []
        for pedido in self.pedidos:
            if pedido.pago != None:
                if isinstance(pedido, PedidoLocal):
                    local = local + pedido.pago.monto_total
                elif isinstance(pedido, PedidoLlevar):
                    llevar = llevar + pedido.pago.monto_total
                else:
                    delivery = delivery + pedido.pago.monto_total
                for producto in pedido.items:
                    if producto.nombre in nombres:
                        i = nombres.index(producto.nombre)
                        cantidades[i] = cantidades[i] + 1
                    else:
                        nombres.append(producto.nombre)
                        cantidades.append(1)
        print("Ventas Local:       Bs " + str(round(local, 2)))
        print("Ventas Para llevar: Bs " + str(round(llevar, 2)))
        print("Ventas Delivery:    Bs " + str(round(delivery, 2)))
        print("Top 3 productos mas vendidos:")
        for puesto in range(3):
            if len(nombres) > 0:
                mayor = cantidades.index(max(cantidades))
                print(str(puesto + 1) + ". " + nombres[mayor] + " - " + str(cantidades[mayor]))
                nombres.pop(mayor)
                cantidades.pop(mayor)


    def ejecutar(self):
        opcion = ""
        while opcion != "0":
            print("")
            print("===== SABOR VALLUNO =====")
            print("1. Ver menu del dia")
            print("2. Registrar producto")
            print("3. Armar combo")
            print("4. Registrar cliente")
            print("5. Nuevo pedido")
            print("6. Quitar producto de un pedido")
            print("7. Ver detalle de un pedido")
            print("8. Cambiar estado de un pedido")
            print("9. Cobrar pedido")
            print("10. Reporte de ventas")
            print("0. Salir")
            opcion = input("Opcion: ")
            try:
                if opcion == "1":
                    self.mostrar_menu()
                elif opcion == "2":
                    self.registrar_producto()
                elif opcion == "3":
                    self.armar_combo()
                elif opcion == "4":
                    self.registrar_cliente()
                elif opcion == "5":
                    self.nuevo_pedido()
                elif opcion == "6":
                    self.quitar_producto()
                elif opcion == "7":
                    self.ver_detalle()
                elif opcion == "8":
                    self.cambiar_estado()
                elif opcion == "9":
                    self.cobrar()
                elif opcion == "10":
                    self.reporte()
            except ValueError as error:

                print("Error: " + str(error))
        print("Gracias por visitar Sabor Valluno")


dia_de_hoy = input("Que dia es hoy? (lunes, martes...): ").lower()
sistema = SistemaPedidos(dia_de_hoy)
sistema.ejecutar()
