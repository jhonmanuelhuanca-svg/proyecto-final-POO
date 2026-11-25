class MetodoPago:
    permite_delivery =True

    def __init__(self):
        self._monto_total = 0

    @property
    def monto_total(self):
        return self._monto_total    

    def procesar_pago(self, total):
        self._monto_total = total

class PagoQR(MetodoPago):
    def __init__(self, codigo_transaccion):
        super().__init__()
        if not self.validar_cod(codigo_transaccion):
            raise ValueError("Codigo de transaccion debe tener 10 digitos")
        self.__codigo_trasaccion = codigo_transaccion

class PagoEfectivo(MetodoPago):

    def __init__(self, monto_recibido):
        super().__init__()
        self.monto_recibido = monto_recibido

    def calcular_cambio(self):
        return round(self.monto_recibido - self.monto_total, 2)

    def procesar_pago(self, total):
        if self.monto_recibido < total:
            raise ValueError("El monto recibido no cubre el total de la compra." + str(total))
        self._monto_total = total

class PagoTarjeta(MetodoPago):
    permite_delivery = False

    def __init__(self):
        super().__init__()
        self.__comision = 0

    def calcular_comision(self, total):
        return round(total * 0.03, 2)

    def procesar_pago(self, total):
        self.__comision = self.calcular_comision(total)
        self._monto_total = round(total + self.__comision, 2)

