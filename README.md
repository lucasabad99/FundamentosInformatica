# 🏧 Cajero Automático — Trabajo Práctico Grupo 05

Simulación de un cajero automático desarrollada en Python como trabajo práctico universitario. El programa permite configurar los billetes disponibles, calcular la cantidad mínima de billetes para entregar un monto solicitado, y mostrar un resumen final de todas las operaciones realizadas.

---

## 📋 Tabla de contenidos

- [Descripción del problema](#descripción-del-problema)
- [Funcionalidades](#funcionalidades)
- [Estructura del código](#estructura-del-código)
- [Constantes](#constantes)
- [Funciones](#funciones)
- [Programa principal](#programa-principal)
- [Algoritmos utilizados](#algoritmos-utilizados)
- [Ejemplos de uso](#ejemplos-de-uso)
- [Restricciones y validaciones](#restricciones-y-validaciones)
- [Consideraciones de diseño](#consideraciones-de-diseño)

---

## Descripción del problema

Un banco necesita un programa para sus cajeros automáticos que lea una cantidad de dinero e imprima a cuántos billetes equivale, minimizando la cantidad de billetes entregados.

El programa fue diseñado para ser adaptable a distintas monedas (modelo de exportación), por lo que los valores de los billetes no están fijos en el código sino que se ingresan al inicio de cada ejecución.

El flujo general es:

1. El operador ingresa uno a uno los valores de billetes disponibles (en cualquier orden), finalizando con `-1`.
2. El programa solicita montos a entregar de forma repetida hasta que se ingresa `-1`.
3. Al finalizar, se muestra un resumen de todas las operaciones ordenado de mayor a menor según el monto entregado.

---

## Funcionalidades

- Carga de billetes disponibles con validación de rango, duplicados y cantidad máxima.
- Ordenamiento automático de billetes de mayor a menor.
- Cálculo de la combinación óptima (mínima cantidad de billetes) para cualquier monto.
- Detección y reporte de montos que no pueden entregarse exactamente.
- Registro de todas las operaciones exitosas.
- Resumen final ordenado de mayor a menor por monto.

---

## Estructura del código

```
cajero.py
│
├── CONSTANTES
│   ├── BILLETE_MINIMO
│   ├── BILLETE_MAXIMO
│   ├── MINIMO_BILLETES
│   └── MAXIMO_BILLETES
│
├── FUNCIONES DE VALIDACIÓN
│   ├── billete_en_rango()
│   ├── billete_repetido()
│   ├── lista_llena()
│   ├── lista_vacia()
│   └── monto_valido()
│
├── FUNCIONES DE CARGA Y ORDENAMIENTO
│   ├── cargar_billetes()
│   ├── ordenar_mayor_a_menor()
│   └── ordenar_operaciones_mayor_a_menor()
│
├── FUNCIÓN PRINCIPAL DE CÁLCULO
│   └── calcular_billetes_para_monto()
│
├── FUNCIONES DE VISUALIZACIÓN
│   ├── mostrar_billetes()
│   ├── mostrar_resultado_monto()
│   └── mostrar_resumen_operaciones()
│
└── PROGRAMA PRINCIPAL
```

---

## Constantes

```python
BILLETE_MINIMO = 10
BILLETE_MAXIMO = 20000
MINIMO_BILLETES = 1
MAXIMO_BILLETES = 10
```

Las constantes centralizan los parámetros configurables del sistema. En lugar de escribir valores literales en distintas partes del código ("números mágicos"), se usan nombres descriptivos. Si se necesita ajustar algún límite, solo se modifica una línea.

| Constante        | Valor | Significado                                      |
|------------------|-------|--------------------------------------------------|
| `BILLETE_MINIMO` | 10    | Valor mínimo aceptado para un billete            |
| `BILLETE_MAXIMO` | 20000 | Valor máximo aceptado para un billete            |
| `MINIMO_BILLETES`| 1     | Cantidad mínima de billetes que debe haber       |
| `MAXIMO_BILLETES`| 10    | Cantidad máxima de billetes distintos permitidos |

---

## Funciones

### `billete_en_rango(billete)`

Verifica que el billete ingresado esté dentro del rango permitido por las constantes.

- **Parámetro:** `billete` — valor entero ingresado por el usuario.
- **Retorna:** `1` si el billete es válido, `0` si está fuera de rango.

```python
# Lógica central
if billete < BILLETE_MINIMO or billete > BILLETE_MAXIMO:
    valido = 0
```

Se usa `or` porque alcanza con que una sola condición sea verdadera para que el billete sea inválido.

---

### `billete_repetido(billete, lista_billetes)`

Recorre la lista de billetes ya cargados para verificar que no se ingrese el mismo valor dos veces.

- **Parámetros:** `billete` — valor a verificar; `lista_billetes` — lista actual de billetes.
- **Retorna:** `1` si el billete ya existe en la lista, `0` si no.

La búsqueda se detiene en cuanto encuentra una coincidencia, evitando recorridos innecesarios.

---

### `lista_llena(lista_billetes)`

Controla que no se supere el máximo de billetes distintos permitidos (`MAXIMO_BILLETES`).

- **Parámetro:** `lista_billetes` — lista actual.
- **Retorna:** `1` si la lista está llena, `0` si aún tiene espacio.

---

### `lista_vacia(lista_billetes)`

Verifica que haya al menos un billete cargado antes de continuar.

- **Parámetro:** `lista_billetes` — lista actual.
- **Retorna:** `1` si la lista está vacía, `0` si tiene al menos un elemento.

---

### `monto_valido(monto)`

Verifica que el monto ingresado sea mayor a cero.

- **Parámetro:** `monto` — entero ingresado por el usuario.
- **Retorna:** `1` si es válido, `0` si no lo es.

---

### `cargar_billetes()`

Función interactiva que lee los billetes disponibles uno por uno hasta que el usuario ingresa `-1`.

Aplica todas las validaciones en orden:

1. No permite salir si la lista sigue vacía.
2. Rechaza billetes cuando la lista ya está llena.
3. Rechaza billetes fuera de rango.
4. Rechaza billetes ya ingresados.
5. Solo agrega el billete si pasa todas las validaciones.

La condición del bucle es:

```python
while entrada != -1 or len(lista_billetes) == 0:
```

Esto garantiza que el usuario no pueda terminar sin haber cargado al menos un billete: aunque escriba `-1`, si la lista está vacía, el ciclo continúa.

- **Retorna:** lista con los billetes cargados.

---

### `ordenar_mayor_a_menor(lista)`

Ordena una copia de la lista de billetes de mayor a menor usando el algoritmo Bubble Sort.

- **Parámetro:** `lista` — lista de billetes a ordenar.
- **Retorna:** nueva lista ordenada de mayor a menor (la original no se modifica).

Trabaja sobre una copia para no alterar la lista original:

```python
copia = []
i = 0
while i < len(lista):
    copia.append(lista[i])
    i = i + 1
```

El ordenamiento de mayor a menor es clave para que luego el algoritmo voraz de `calcular_billetes_para_monto()` funcione correctamente.

---

### `ordenar_operaciones_mayor_a_menor(operaciones)`

Ordena la lista de operaciones según el monto entregado, de mayor a menor.

- **Parámetro:** `operaciones` — lista de pares `[monto, resultado]`.
- **Retorna:** copia de la lista ordenada por `operacion[0]` (el monto).

Usa el mismo algoritmo Bubble Sort que `ordenar_mayor_a_menor()`, comparando el primer elemento de cada operación.

---

### `calcular_billetes_para_monto(monto, billetes_ordenados)`

Es la función más importante del programa. Calcula cuántos billetes de cada denominación se necesitan para entregar exactamente el monto solicitado, usando la menor cantidad posible de billetes.

- **Parámetros:** `monto` — entero a entregar; `billetes_ordenados` — lista de billetes ya ordenada de mayor a menor.
- **Retorna:** lista de pares `[billete, cantidad]` si el monto puede formarse exactamente, o lista vacía `[]` si no es posible.

**Estrategia (algoritmo voraz / greedy):**

```python
cantidad = resto // billete   # Máxima cantidad de este billete que cabe
resto = resto % billete       # Lo que queda por cubrir
```

Primero se usan los billetes más grandes, tomando la mayor cantidad posible de cada uno. Luego se continúa con los más pequeños hasta cubrir el monto o agotar las opciones.

Si al finalizar el recorrido `resto != 0`, significa que quedó dinero que no puede representarse con los billetes disponibles, y se retorna una lista vacía para señalizar el error.

**Ejemplo paso a paso con monto $2200 y billetes [500, 200, 100]:**

| Billete | División entera        | Resto restante      |
|---------|------------------------|---------------------|
| $500    | 2200 // 500 = **4**    | 2200 % 500 = 200    |
| $200    | 200 // 200 = **1**     | 200 % 200 = 0       |
| $100    | (no se necesita)       | —                   |

Resultado: `[[500, 4], [200, 1]]` → 5 billetes en total.

---

### `mostrar_billetes(lista_billetes)`

Imprime en pantalla los billetes disponibles en una sola línea separada por comas.

---

### `mostrar_resultado_monto(monto, resultado)`

Imprime el detalle de billetes utilizados para un monto específico, mostrando billete, cantidad y subtotal.

Ejemplo de salida:

```
Monto $2200:
  $500 x 4 = $2000
  $200 x 1 = $200
```

---

### `mostrar_resumen_operaciones(operaciones)`

Muestra el resumen final de todas las operaciones exitosas, ordenadas de mayor a menor por monto. Si no hubo ninguna operación, lo informa.

---

## Programa principal

El programa principal coordina el flujo general en tres etapas:

**Etapa 1 — Configuración:**
```python
lista_billetes = cargar_billetes()
billetes_ordenados = ordenar_mayor_a_menor(lista_billetes)
mostrar_billetes(billetes_ordenados)
```

**Etapa 2 — Operaciones:**
```python
while monto != -1:
    if monto_valido(monto) == 1:
        resultado = calcular_billetes_para_monto(monto, billetes_ordenados)
        if len(resultado) == 0:
            # Error: monto no puede entregarse
        else:
            mostrar_resultado_monto(monto, resultado)
            operaciones.append([monto, copia_resultado])
```

Se guarda una copia del resultado en cada operación para que modificaciones futuras en la lista no afecten el historial.

**Etapa 3 — Resumen:**
```python
mostrar_resumen_operaciones(operaciones)
```

---

## Algoritmos utilizados

### Bubble Sort (Ordenamiento Burbuja)

Usado en `ordenar_mayor_a_menor()` y `ordenar_operaciones_mayor_a_menor()`.

Compara elementos adyacentes e intercambia si están en el orden incorrecto. Repite el proceso hasta que la lista quede ordenada.

```python
if copia[j] < copia[j + 1]:   # Para orden descendente
    aux = copia[j]
    copia[j] = copia[j + 1]
    copia[j + 1] = aux
```

La variable auxiliar `aux` es imprescindible para no perder el valor que se desplaza.

### Algoritmo Voraz (Greedy)

Usado en `calcular_billetes_para_monto()`.

Toma siempre la decisión localmente óptima: usar la mayor cantidad posible del billete más grande disponible antes de pasar al siguiente. Esto garantiza la menor cantidad de billetes cuando los valores de los billetes permiten una solución exacta.

---

## Ejemplos de uso

### Ejemplo del enunciado

**Billetes ingresados:** 200, 500, 100  
**Montos solicitados:** 2200, 3500, 920, 600

```
Monto $2200:
  $500 x 4 = $2000
  $200 x 1 = $200

Monto $3500:
  $500 x 7 = $3500

Error: no es posible entregar $920 con los billetes disponibles.

Monto $600:
  $500 x 1 = $500
  $100 x 1 = $100
```

**Resumen final (ordenado de mayor a menor):**

```
RESUMEN DE OPERACIONES

Monto entregado: $3500
  $500 x 7

Monto entregado: $2200
  $500 x 4
  $200 x 1

Monto entregado: $600
  $500 x 1
  $100 x 1
```

El monto de $920 no aparece en el resumen porque no pudo entregarse.

### ¿Por qué $920 genera error?

Con billetes de $500, $200 y $100:

| Billete | División entera   | Resto |
|---------|-------------------|-------|
| $500    | 920 // 500 = 1    | 420   |
| $200    | 420 // 200 = 2    | 20    |
| $100    | 20 // 100 = 0     | 20    |

Queda un resto de $20 que no puede representarse con ningún billete disponible → error.

---

## Restricciones y validaciones

| Situación                        | Comportamiento                              |
|----------------------------------|---------------------------------------------|
| Billete menor a $10              | Error, se vuelve a pedir                    |
| Billete mayor a $20000           | Error, se vuelve a pedir                    |
| Billete ya ingresado             | Error, se vuelve a pedir                    |
| Más de 10 billetes distintos     | Error, no se agrega                         |
| Intentar salir sin billetes      | No se permite, se exige al menos uno        |
| Monto igual o menor a cero       | Error, se vuelve a pedir                    |
| Monto que no puede formarse      | Error informativo, no se registra           |

---

## Consideraciones de diseño

- **Separación en funciones:** cada función tiene una única responsabilidad, lo que facilita la lectura, las pruebas y el mantenimiento.
- **Sin modificación de datos originales:** las funciones de ordenamiento trabajan sobre copias, preservando las listas originales.
- **Historial de operaciones con copia:** al guardar cada operación, se copia el resultado para que cambios posteriores no afecten el registro.
- **Adaptabilidad a distintas monedas:** los billetes se ingresan en tiempo de ejecución, sin valores fijos en el código.
- **Código dentro del currículum:** el programa utiliza exclusivamente estructuras básicas — funciones, listas, bucles `while`, operadores `//` y `%` — sin `break`, `continue`, slicing ni valores booleanos literales.
