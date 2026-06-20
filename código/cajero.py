# TRABAJO PRACTICO - GRUPO 05
# CAJERO AUTOMATICO

BILLETE_MINIMO = 10
BILLETE_MAXIMO = 20000
MINIMO_BILLETES = 1
MAXIMO_BILLETES = 10

# FUNCIONES

def billete_en_rango(billete):
    valido = 1
    if billete < BILLETE_MINIMO or billete > BILLETE_MAXIMO:
        print("Error: el billete $", billete, "no es valido. Debe estar entre $", BILLETE_MINIMO, " y $", BILLETE_MAXIMO)
        valido = 0
    return valido


def billete_repetido(billete, lista_billetes):
    repetido = 0
    i = 0
    while i < len(lista_billetes) and repetido == 0:
        if lista_billetes[i] == billete:
            print("Error: el billete $", billete, "ya fue ingresado.")
            repetido = 1
        i = i + 1
    return repetido


def lista_llena(lista_billetes):
    llena = 0
    if len(lista_billetes) == MAXIMO_BILLETES:
        print("Error: ya se ingresaron el maximo de", MAXIMO_BILLETES, "billetes.")
        llena = 1
    return llena


def lista_vacia(lista_billetes):
    vacia = 0
    if len(lista_billetes) < MINIMO_BILLETES:
        vacia = 1
    return vacia


def monto_valido(monto):
    valido = 1
    if monto <= 0:
        print("Error: el monto debe ser mayor a cero.")
        valido = 0
    return valido


def cargar_billetes():
    lista_billetes = []
    print("Ingrese los billetes disponibles uno a uno.")
    print("Escriba -1 para terminar.")

    while len(lista_billetes) < MAXIMO_BILLETES:
        entrada = int(input("Billete: "))

        if entrada == -1:
            if len(lista_billetes) == 0:
                print("Debe ingresar al menos un billete.")
            else:
                break
        elif billete_en_rango(entrada) == 0:
            continue
        elif billete_repetido(entrada, lista_billetes) == 1:
            continue
        else:
            lista_billetes.append(entrada)
            print("Billete $", entrada, "agregado. Total ingresados:", len(lista_billetes))
            if len(lista_billetes) == MAXIMO_BILLETES:
                print("Se ha alcanzado el límite máximo. Finalizando carga...")
                break

    return lista_billetes

def ordenar_mayor_a_menor(lista):
    copia = []
    i = 0
    while i < len(lista):
        copia.append(lista[i])
        i = i + 1

    n = len(copia)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if copia[j] < copia[j + 1]:
                aux = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = aux
            j = j + 1
        i = i + 1

    return copia


def ordenar_operaciones_mayor_a_menor(operaciones):
    copia = []
    i = 0
    while i < len(operaciones):
        copia.append(operaciones[i])
        i = i + 1

    n = len(copia)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if copia[j][0] < copia[j + 1][0]:
                aux = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = aux
            j = j + 1
        i = i + 1

    return copia


def calcular_billetes_para_monto(monto, billetes_ordenados):
    resultado = []
    resto = monto
    i = 0

    while i < len(billetes_ordenados) and resto > 0:
        billete = billetes_ordenados[i]
        cantidad = resto // billete
        if cantidad > 0:
            resultado.append([billete, cantidad])
            resto = resto % billete
        i = i + 1

    if resto != 0:
        resultado = []

    return resultado


def mostrar_billetes(lista_billetes):
    print()
    print("Billetes disponibles: ", end="")
    i = 0
    while i < len(lista_billetes):
        print("$" + str(lista_billetes[i]), end="")
        if i < len(lista_billetes) - 1:
            print(", ", end="")
        i = i + 1
    print()


def mostrar_resultado_monto(monto, resultado):
    print()
    print("Monto $", monto, ":")
    i = 0
    while i < len(resultado):
        billete = resultado[i][0]
        cantidad = resultado[i][1]
        print("$", billete, "x", cantidad, "= $", billete * cantidad)
        i = i + 1


def mostrar_resumen_operaciones(operaciones):
    if len(operaciones) == 0:
        print()
        print("No se realizo ninguna operacion.")
        return

    operaciones_ordenadas = ordenar_operaciones_mayor_a_menor(operaciones)
    print()
    print("RESUMEN DE OPERACIONES")

    i = 0
    while i < len(operaciones_ordenadas):
        monto = operaciones_ordenadas[i][0]
        resultado = operaciones_ordenadas[i][1]
        print()
        print("Monto entregado: $", monto)
        j = 0
        while j < len(resultado):
            billete = resultado[j][0]
            cantidad = resultado[j][1]
            print("$", billete, "x", cantidad)
            j = j + 1
        i = i + 1


# PROGRAMA PRINCIPAL

print("CAJERO AUTOMATICO")
lista_billetes = cargar_billetes()
billetes_ordenados = ordenar_mayor_a_menor(lista_billetes)
mostrar_billetes(billetes_ordenados)

operaciones = []
print()
print("Ingrese los montos a entregar.")
print("Escriba -1 para terminar y ver el resumen.")
print()

monto = int(input("Monto: "))

while monto != -1:
    if monto_valido(monto) == 1:
        resultado = calcular_billetes_para_monto(monto, billetes_ordenados)
        if len(resultado) == 0:
            print("Error: no es posible entregar $", monto, "con los billetes disponibles.")
        else:
            mostrar_resultado_monto(monto, resultado)
            copia_resultado = []
            i = 0
            while i < len(resultado):
                copia_resultado.append(resultado[i])
                i = i + 1
            operaciones.append([monto, copia_resultado])

    print()
    monto = int(input("Monto: "))

mostrar_resumen_operaciones(operaciones)