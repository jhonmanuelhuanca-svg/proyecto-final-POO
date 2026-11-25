# Bitácora de uso de IA

**Proyecto:** Sistema de Pedidos Sabor Valluno
**Estudiante:** __Ronaldo Bautista Nina
**Variante:** C
**Herramienta usada:** Claude (asistente de IA de Anthropic)

> Las columnas **"Qué modifiqué yo"** y **"¿Lo explico sin ayuda?"** las completa el estudiante.
> En "¿Lo explico sin ayuda?" escribir: **Sí**, **En parte** o **No**.

## Registro

| N.º | Fecha | Herramienta | Tipo de uso | Consulta textual | Qué acepté | Qué modifiqué yo y por qué | Archivo o clase | ¿Lo explico sin ayuda? |
|---|---|---|---|---|---|---|---|---|
| 1 | 11/11/2026 | Claude | Explicación | "nesesito hacer sobre un proyecto, y por hoy tengo que hacer diagramas subire el documento" | Resumen del documento y lista de diagramas posibles (clases, estados, casos de uso) | | Documento del proyecto | |
| 2 | 11/11/2026 | Claude | Explicación | "atributos privados, publicos, metodos en mi caso soy el estudiante, y por hoy ayudeme a haver la diagrama" | Explicación de la notación UML (visibilidad `-` `#` `+`, herencia, composición, agregación, multiplicidades) y pasos para armar el diagrama | | Diagrama de clases | |
| 3 | 11/11/2026 | Claude | Explicación | "explique cua como cuales son las clases padre hija atributos y para generarlas respuestas" / "cual es la classe principal de acuerdo a eso ponme en orden" | Explicación de clase padre e hija, técnica de sustantivos y verbos, y orden de las clases | | Diagrama de clases | |
| 4 | 11/11/2026 | Claude | Generación | "le preginte y me dijo que si, ya lo anote" (después de pedir el diagrama completo con la variante C) | Diagrama de clases completo, de estados y de casos de uso en PDF y PNG | | docs/ (diagramas) | |
| 5 | 11/11/2026 | Claude | Generación | "me lo genera en fromatom drawio y que sea entendible" / "me puede generar otro diagrama nuevo basico como para que entre todo a un cuaderno" / "mejor genera un poco mas completo" | Diagrama de clases en draw.io, versión ordenada del 1 al 8, versión básica y versión media para copiar en el cuaderno | | docs/ (diagramas) | |
| 6 | 11/11/2026 | Claude | Explicación | "del primer drawio que generaste expliqueme su classe y sus atributos" / "expliqueme sobre la parte de pedido" / "pedidos deliveri" / "clas producto" | Explicación de las clases Restaurante, Pedido, PedidoDelivery y Producto, con ejemplos de cálculo de la variante C | | Pedido, PedidoDelivery, Producto, Combo | |
| 7 | 13/11/2026 | Claude | Revisión | "subire una diagrma y verificaras como esta okey" | Lista de correcciones a mi diagrama hecho a mano (combo duplicado, atributos repetidos, tipos, flechas de herencia, valores de la variante C) | | Diagrama v1 (cuaderno) | |
| 8 | 13/11/2026 | Claude | Generación | "me lo mejora mi diagrama a la misma base con lo que crees que falta... y genera en formato drawio" | Mi diagrama corregido en draw.io, manteniendo mi distribución y mis nombres | | docs/ (diagrama) | |
| 9 | 13/11/2026 | Claude | Generación | "en classe producto lo que es la clase combo, dise que tambien tiene que a ver otro clase comboProducto haci como en la imajen" | Diagrama con la clase ComboProducto y la nota de validación, como lo dibujó el docente en la pizarra | | Combo, ComboProducto | |
| 10 | 13/11/2026 | Claude | Generación | "m dosente dijo que la classe restaurante no tiene relacion con ninguno osea no existe" | Diagrama sin la clase Restaurante | | docs/ (diagrama) | |
| 11 | 18/11/2026 | Claude | Revisión | (foto del diagrama sellado por el docente) | Lista de pendientes para el diagrama v2 | | Diagrama v1 sellado | |
| 12 | 18/11/2026 | Claude | Explicación | "Ayudeme a hacer la clase producto que tenemos hay indíqueme como hacerlo" / "Colo sería el método calcular_precio" | Explicación de la clase Producto y del método calcular_precio en cada subclase | | Producto, Plato, Bebida, Combo | |
| 13 | 18/11/2026 | Claude | Generación | "Haber realiza todo el código de todo el proyecto" | Código completo: modelo/, main.py, pruebas.py, README, acta y bitácora | | Todo el proyecto | |
| 14 | 23/11/2026 | Claude | Corrección | "el codigo tiene que ser todo lo que se hace en programacion orientada a objetos" | main.py y pruebas.py pasados a clases | | main.py, pruebas.py | |
| 15 | 23/11/2026 | Claude | Corrección | "el codigo tiene que ser deacuerdo a la diagrma... y no tiene que tener importaciones de libreria por que a un no pasamos esa parte" | Código sin librerías y con los nombres del diagrama sellado | | modelo/, main.py | |
| 16 | 23/11/2026 | Claude | Corrección | "tiene que tener input... solo utilizamos lo que estamos viendo o lo que aparece en el video que subi" | Código con input() y solo con lo que aparece en el video de clase (sin try/except, diccionarios ni f-strings) | | Todo el proyecto | |
| 17 | 23/11/2026 | Claude | Corrección | "yo me referia a que podamos ingresar los datos a que los clientes pueden pedir... por ejemplo la cantidad" | Menú del restaurante ya cargado; el input es para lo que pide el cliente | | main.py | |
| 18 | 23/11/2026 | Claude | Corrección | (fotos de la sección 4 y de las reglas de negocio) "tiene que ser algo haci tambien como piede clase abstracta y recuerda que es con la variante c" / "masomenos tiene que tener esta logica pero tiene que ser igual que la diagrama con sello" | Ajuste a la rúbrica y a las reglas: contar_platos(), excepción en cambios de estado inválidos, chicharrón solo domingos, nombres del diagrama | | modelo/, pruebas.py | |
| 19 | 23/11/2026 | Claude | Corrección | (foto de la rúbrica) "y esta es para que sea una calificacion exelente" | Setters con ValueError, las 7 funciones en el menú, descuentos en el detalle, diagrama v2 | | modelo/, main.py, docs/diagrama_v2 | |
| 20 | 23/11/2026 | Claude | Corrección | "pero tiene cumplir con esta esta es la oficial firmado con el docente el codigo tiene que salir de esta diagrama" / "como la clase pricipal seria pedido..." | Se quitaron métodos extra no obligatorios y se ordenaron las clases con Pedido primero | | modelo/ | |
| 21 | 23/11/2026 | Claude | Corrección | "tiene que funcionar con herencia ya dije que no importar librerias" / "entonces que no sea abstracta haci no sale el error" | Se quitó `abc`; las clases padre ya no son abstractas (el docente lo autorizó, ver acta) | | Pedido, Producto, MetodoPago | |
| 22 | 23/11/2026 | Claude | Corrección | "pero esa parte de main.py no habnazamo casi no le entiendo" → opción "1" (simplificarlo) | main.py más corto y simple | | main.py | |
| 23 | 24/11/2026 | Claude | Generación | "oye como seria mi diagrama con el codigo que generaste a base de la diagrama con sello" / "tiene que estar dibujado la diagrama de esta forma" | Diagrama v2 en PNG con la misma distribución que el diagrama sellado | | docs/diagrama_v2.png | |
| 24 | 24/11/2026 | Claude | Corrección | "lo tenemos que sacar la clase item pedido lo demas tiene que ser lo mismo... tiene que cumplir con la diagrma a con sello... y tiene que ser como en el video" | Código sin ItemPedido, con los atributos y métodos del diagrama sellado; diagrama v2 actualizado | | modelo/, main.py, pruebas.py, docs/ | |
| 25 | 24/11/2026 | Claude | Generación | "genera el formato en formato drawio" | Diagrama v2 en draw.io con la distribución del diagrama sellado | | docs/diagrama_v2.drawio | |
| 26 | 25/11/2026 | Claude | Generación | "me puedes generar la vitacora" | Esta bitácora (las columnas de modificaciones y explicación las completo yo) | | docs/bitacora_ia.md | |

## Resumen

- **Diagrama:** el diagrama v1 lo dibujé a mano en el cuaderno y lo selló el docente. La IA revisó el v1 y generó el diagrama v2 a partir del código.
- **Código:** la IA generó el código y lo fue corrigiendo según mis indicaciones y las del docente (sin librerías, sin clase Restaurante, sin ItemPedido, clases padre no abstractas, menú con input).
- **Pendiente de consultar al docente:** la regla 9 (retraso en delivery) y cómo se cuentan los envases de un combo para llevar (ver `docs/acta_consultas.md`).
