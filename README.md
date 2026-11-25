# Sistema de Pedidos Sabor Valluno (Variante C)

Proyecto integrador de Programación Orientada a Objetos. Aplicación de consola en Python 3
(sin librerías externas).

**Universidad:** Universidad Adventista de Bolivia (UAB) · Ingeniería de Sistemas
**Integrantes:** [Nombre del estudiante 1], [Nombre del estudiante 2]
**Docente:** [Nombre del docente] · **Gestión:** 2026

## Cómo ejecutar

```
python main.py      # menú de consola
python pruebas.py   # casos de prueba
```

## Estructura

La clase central es `Pedido`. Alrededor de ella están las otras clases principales
(`Cliente`, `Producto` y `Pago`), igual que en el diagrama:

```
Pedido (clase central)
├── PedidoLocal, PedidoLlevar, PedidoDelivery
├── items ◇── Producto          (los productos que pide el cliente)
├── EstadoPedido
├── ──→ Cliente                 (quien hace el pedido)
└── ──→ Pago                    (como se paga)

Producto
├── Plato
├── Bebida
└── Combo ◆── ComboProducto
```

```
modelo/
  pedido.py      Pedido, PedidoLocal, PedidoLlevar, PedidoDelivery, EstadoPedido
  cliente.py     Cliente
  producto.py    Producto, Plato, Bebida, Combo, ComboProducto
  pago.py        Pago (monto recibido, cambio y comprobante)
main.py          clase SistemaPedidos (menú de consola con input)
pruebas.py       clase Pruebas (14 pruebas con assert)
docs/
  diagrama_v2.drawio / .png   Diagrama de clases final
  bitacora.md                 Bitácora del proyecto
  bitacora_ia.md              Bitácora de uso de IA
  registro_ia_*.md            Registro individual de consultas a IA
```

## Reglas de la Variante C

| Regla | Valor | Dónde está |
|---|---|---|
| Descuento del combo | 8 % | `Combo.DESCUENTO` |
| Envase para llevar | Bs 1,50 por producto | `PedidoLlevar.COSTO_ENVASE` |
| Envío gratis | Desde Bs 200, solo Cercado | `PedidoDelivery.ENVIO_GRATIS` |
| Pedido mínimo delivery | Bs 35 | `PedidoDelivery.PEDIDO_MINIMO` |
| Regla adicional | Combo con máximo 4 productos | `Combo.MAX_PRODUCTOS` |

## Pilares de la POO

| Pilar | Cómo se cumple |
|---|---|
| Encapsulación | Atributos `_protegidos` (`#`) y `__privados` (`-`) como en el diagrama; lectura con `@property`; las reglas 6 y 8 lanzan `ValueError` con mensajes claros; la lista `items` solo cambia con `agregar_producto()` / `quitar_producto()` |
| Herencia | `Pedido` → `PedidoLocal`, `PedidoLlevar`, `PedidoDelivery`; `Producto` → `Plato`, `Bebida`, `Combo`. Todas usan `super().__init__()`; `PedidoDelivery.pagar()` extiende al padre con `super().pagar()`; `Bebida` hereda `esta_disponible()` sin cambiarlo |
| Polimorfismo | `calcular_precio()`, `esta_disponible()` y `calcular_cargos()` se sobrescriben; `Pedido.calcular_total()` suma los precios sin preguntar el tipo de producto; `Combo.calcular_precio()` funciona aunque contenga otro combo |
| Abstracción | Por indicación del docente, las clases padre no son abstractas: tienen métodos generales que las subclases sobrescriben |

No se importa ninguna librería: solo se conectan los archivos propios de `modelo/`.

## Opciones del menú (main.py)

| Opción | Función |
|---|---|
| 1, 2, 3 | Productos: ver el menú del día, registrar un plato o bebida, armar un combo |
| 4 | Clientes: registrar un cliente |
| 5, 6 | Pedidos: nuevo pedido (local, para llevar o delivery) con productos y cantidades; quitar un producto |
| 7 | Detalle: productos, descuentos, subtotal, cargos y total |
| 8 | Estados: EN_PREPARACION, LISTO, ENTREGADO o CANCELADO |
| 9 | Cobro: efectivo (con cambio), QR o tarjeta, con comprobante |
| 10 | Reporte: ventas por tipo de pedido y top 3 de productos |

El menú del restaurante ya viene cargado. Si una regla no se cumple, el modelo lanza
`ValueError`, `main.py` muestra el mensaje y el programa sigue.

## Diagramas

- `docs/diagrama_v1`: foto del diagrama sellado por el docente (agregar la imagen).
- `docs/diagrama_v2.drawio` y `docs/diagrama_v2.png`: diagrama final, coincide con el
  código; incluye la nota "Cambios respecto al diagrama v1" con cada cambio explicado.

## Uso de IA

Las consultas a herramientas de IA están registradas en `docs/bitacora_ia.md` y en los
registros individuales de `docs/`, indicando qué se pidió, qué se aplicó y qué se modificó.

## Pendiente

- Regla 9 (retraso en delivery): completar `PedidoDelivery.minutos_retraso` y la
  compensación con la respuesta del docente.
