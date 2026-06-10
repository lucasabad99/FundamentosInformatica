# TRABAJO PRÁCTICO - GRUPO 05
# CAJERO AUTOMÁTICO

---

# DESCRIPCIÓN GENERAL

El programa simula el funcionamiento de un cajero automático.

Permite:

- Ingresar las denominaciones de billetes disponibles.
- Validar que los billetes sean correctos.
- Ordenar los billetes de mayor a menor.
- Solicitar montos a entregar.
- Calcular la menor cantidad posible de billetes para cada monto.
- Informar error cuando un monto no puede entregarse exactamente.
- Guardar todas las operaciones realizadas.
- Mostrar un resumen final ordenado de mayor a menor según el monto.

---

# ESTRUCTURA GENERAL DEL PROGRAMA

El programa está dividido en tres partes:

1. Constantes.
2. Funciones.
3. Programa principal.

---

# 1. CONSTANTES

```python
BILLETE_MINIMO = 10
BILLETE_MAXIMO = 20000
MINIMO_BILLETES = 1
MAXIMO_BILLETES = 10
```

## ¿Para qué sirven?

Evitan escribir números "mágicos" en todo el programa.

Por ejemplo:

```python
if billete < BILLETE_MINIMO
```

es más claro que:

```python
if billete < 10
```

Además, si cambia el valor mínimo permitido, solo se modifica una línea.

---

# 2. FUNCIÓN billete_en_rango()

```python
def billete_en_rango(billete):
```

## ¿Qué hace?

Verifica que el billete ingresado esté entre los límites permitidos.

Ejemplo:

```python
billete_en_rango(500)
```

Resultado:

```python
1
```

Ejemplo:

```python
billete_en_rango(50000)
```

Resultado:

```python
0
```

---

## Funcionamiento

```python
valido = 1
```

Se supone inicialmente que el billete es válido.

---

```python
if billete < BILLETE_MINIMO or billete > BILLETE_MAXIMO:
```

Pregunta:

- ¿Es menor que 10?
- ¿Es mayor que 20000?

Si alguna respuesta es sí:

```python
valido = 0
```

---

```python
return valido
```

Devuelve:

- 1 → válido
- 0 → inválido

---

# 3. FUNCIÓN billete_repetido()

```python
def billete_repetido(billete, lista_billetes):
```

## ¿Qué hace?

Busca si un billete ya fue cargado anteriormente.

---

Ejemplo:

```python
lista_billetes = [100,200,500]
```

Nuevo billete:

```python
200
```

Resultado:

```python
repetido = 1
```

---

## Funcionamiento

```python
i = 0
```

Comienza en la primera posición.

---

```python
while i < len(lista_billetes)
```

Recorre toda la lista.

---

```python
if lista_billetes[i] == billete
```

Pregunta:

¿El billete actual es igual al que quiero ingresar?

---

Si lo encuentra:

```python
repetido = 1
```

---

# 4. FUNCIÓN cargar_billetes()

```python
def cargar_billetes():
```

## ¿Qué hace?

Permite ingresar los billetes disponibles.

---

Ejemplo:

```text
500
200
100
-1
```

Resultado:

```python
[500,200,100]
```

---

## Funcionamiento

```python
lista_billetes = []
```

Se crea una lista vacía.

---

```python
entrada = int(input("Billete: "))
```

Lee un billete.

---

```python
while entrada != -1 or len(lista_billetes) == 0
```

Significa:

Seguir mientras:

- No se ingrese -1

o

- La lista siga vacía

---

Esto obliga a ingresar al menos un billete.

---

```python
lista_billetes.append(entrada)
```

Agrega el billete al final de la lista.

---

Ejemplo:

Antes:

```python
[500]
```

Después:

```python
[500,200]
```

---

# 5. FUNCIÓN ordenar_mayor_a_menor()

```python
def ordenar_mayor_a_menor(lista):
```

## ¿Qué hace?

Ordena los billetes de mayor a menor.

---

Ejemplo:

Antes:

```python
[100,500,200]
```

Después:

```python
[500,200,100]
```

---

## Método utilizado

Bubble Sort (Método Burbuja).

---

## Funcionamiento

```python
if copia[j] < copia[j+1]
```

Pregunta:

¿El elemento de la izquierda es menor?

---

Si sí:

```python
aux = copia[j]
copia[j] = copia[j+1]
copia[j+1] = aux
```

Intercambia posiciones.

---

# 6. FUNCIÓN calcular_billetes_para_monto()

```python
def calcular_billetes_para_monto(...)
```

## Es la función más importante.

Su objetivo es minimizar la cantidad de billetes entregados.

---

Ejemplo:

Billetes:

```python
[500,200,100]
```

Monto:

```python
2200
```

---

## Paso 1

```python
cantidad = resto // billete
```

Hace:

```python
2200 // 500
```

Resultado:

```python
4
```

Significa:

```text
4 billetes de 500
```

---

## Paso 2

```python
resto = resto % billete
```

Hace:

```python
2200 % 500
```

Resultado:

```python
200
```

Todavía faltan entregar $200.

---

## Paso 3

```python
200 // 200
```

Resultado:

```python
1
```

Significa:

```text
1 billete de 200
```

---

Resultado final:

```python
[
 [500,4],
 [200,1]
]
```

---

# ¿POR QUÉ SE MINIMIZA LA CANTIDAD DE BILLETES?

Porque:

1. Primero se ordenan los billetes de mayor a menor.
2. Se utiliza:

```python
cantidad = resto // billete
```

para tomar la máxima cantidad posible de billetes grandes.
3. Luego se continúa con los billetes más pequeños.

---

Ejemplo:

Monto:

```python
2200
```

Billetes:

```python
500
200
100
```

Resultado:

```text
4 billetes de 500
1 billete de 200
```

Total:

```text
5 billetes
```

---

# ¿POR QUÉ APARECE ERROR SI RESTO != 0?

Ejemplo:

Billetes:

```python
500
200
100
```

Monto:

```python
920
```

Proceso:

```text
500 → sobra 420
200 → sobra 20
100 → sobra 20
```

Queda:

```python
resto = 20
```

No existe billete de 20.

Por eso:

```python
resultado = []
```

y el programa informa error.

---

# 7. FUNCIÓN mostrar_resultado_monto()

## ¿Qué hace?

Muestra los billetes utilizados para un monto.

---

Ejemplo:

```python
[
 [500,4],
 [200,1]
]
```

Muestra:

```text
$500 x 4 = $2000
$200 x 1 = $200
```

---

# 8. LISTA operaciones

## ¿Qué guarda?

Todas las operaciones realizadas.

---

Ejemplo:

```python
[
 [2200, [[500,4],[200,1]]],
 [3500, [[500,7]]],
 [600, [[500,1],[100,1]]]
]
```

---

## ¿Para qué sirve?

Permite generar el resumen final solicitado por el enunciado.

---

# 9. FUNCIÓN ordenar_operaciones_mayor_a_menor()

## ¿Qué hace?

Ordena las operaciones según el monto entregado.

---

Ejemplo:

Antes:

```text
2200
3500
600
```

Después:

```text
3500
2200
600
```

---

# 10. RESUMEN FINAL

## ¿Qué hace?

Muestra todas las operaciones realizadas.

---

Ejemplo:

```text
Monto entregado: $3500
$500 x 7

Monto entregado: $2200
$500 x 4
$200 x 1

Monto entregado: $600
$500 x 1
$100 x 1
```

---

# POSIBLES PREGUNTAS DE DEFENSA

## CONSTANTES

### ¿Por qué usar constantes?

Porque si cambia un valor, solo se modifica una línea.

---

### ¿Qué ventajas tienen?

- Mejor legibilidad.
- Fácil mantenimiento.
- Evitan repetir números.

---

## billete_en_rango()

### ¿Qué recibe?

Un entero que representa un billete.

---

### ¿Qué devuelve?

- 1 → válido.
- 0 → inválido.

---

### ¿Por qué se usa OR?

```python
if billete < 10 or billete > 20000
```

Porque alcanza con que una condición sea verdadera para que el billete sea inválido.

---

## billete_repetido()

### ¿Para qué sirve i?

Para recorrer la lista.

---

### ¿Qué hace len()?

Devuelve la cantidad de elementos.

---

### ¿Qué significa?

```python
lista_billetes[i]
```

Acceder al elemento ubicado en la posición i.

---

## cargar_billetes()

### ¿Por qué la lista comienza vacía?

Porque todavía no se cargó ningún billete.

---

### ¿Qué hace append()?

Agrega un elemento al final de la lista.

---

### ¿Por qué no alcanza con?

```python
while entrada != -1
```

Porque permitiría salir sin cargar ningún billete.

---

## ordenar_mayor_a_menor()

### ¿Qué método utiliza?

Bubble Sort (Burbuja).

---

### ¿Para qué sirve aux?

Permite intercambiar valores sin perder información.

---

### ¿Por qué ordenar de mayor a menor?

Porque después se utilizan primero los billetes más grandes.

---

## calcular_billetes_para_monto()

### ¿Qué hace //?

División entera.

Ejemplo:

```python
2200 // 500 = 4
```

---

### ¿Qué hace %?

Obtiene el resto.

Ejemplo:

```python
2200 % 500 = 200
```

---

### ¿Por qué usar // y no /?

Porque no existen cantidades decimales de billetes.

---

### ¿Qué representa resultado?

Ejemplo:

```python
[
 [500,4],
 [200,1]
]
```

Significa:

```text
4 billetes de 500
1 billete de 200
```

---

### ¿Por qué resto != 0 genera error?

Porque quedó dinero sin poder representarse con los billetes disponibles.

---

## operaciones

### ¿Qué guarda?

Todas las operaciones realizadas.

---

### ¿Por qué se guarda?

Porque el enunciado pide mostrar un resumen final.

---

## ordenar_operaciones_mayor_a_menor()

### ¿Por qué se ordenan?

Porque el enunciado pide mostrar las operaciones de mayor a menor según el monto.

---

## PROGRAMA PRINCIPAL

### ¿Por qué dividir el programa en funciones?

Porque:

- Organiza el código.
- Facilita las pruebas.
- Permite reutilizar código.
- Hace más fácil el mantenimiento.

---

# PREGUNTA MÁS IMPORTANTE DEL TP

## ¿Cómo logra el programa minimizar la cantidad de billetes?

Porque:

1. Ordena los billetes de mayor a menor.
2. Utiliza:

```python
cantidad = resto // billete
```

para tomar la máxima cantidad posible de cada denominación.
3. Continúa con el resto utilizando billetes más pequeños.

De esta forma obtiene la menor cantidad posible de billetes para cada monto solicitado.