# ============================================================
# CONSTANTES
# ============================================================
 
BILLETE_MINIMO  = 10
BILLETE_MAXIMO  = 20000
MINIMO_BILLETES = 1
MAXIMO_BILLETES = 10
 
 
# ============================================================
# FUNCIONES DE VALIDACION DE BILLETES
# ============================================================
 
def billete_en_rango(billete):
    valido = 1
    if billete < BILLETE_MINIMO or billete > BILLETE_MAXIMO:
        print("Error: el billete $" + str(billete) +
              " no es valido. Debe estar entre $" +
              str(BILLETE_MINIMO) + " y $" + str(BILLETE_MAXIMO) + ".")
        valido = 0
    return valido
 
 
def billete_repetido(billete, lista_billetes):
    repetido = 0
    i = 0
    while i < len(lista_billetes) and repetido == 0:
        if lista_billetes[i] == billete:
            print("Error: el billete $" + str(billete) + " ya fue ingresado.")
            repetido = 1
        i += 1
    return repetido
 
 
def lista_llena(lista_billetes):
    llena = 0
    if len(lista_billetes) >= MAXIMO_BILLETES:
        print("Error: ya se ingresaron el maximo de " +
              str(MAXIMO_BILLETES) + " billetes.")
        llena = 1
    return llena
 
 
def lista_vacia(lista_billetes):
    vacia = 0
    if len(lista_billetes) < MINIMO_BILLETES:
        print("Debe ingresar al menos " + str(MINIMO_BILLETES) + " billete.")
        vacia = 1
    return vacia
 
 
def monto_valido(monto):
    valido = 1
    if monto <= 0:
        print("Error: el monto debe ser mayor a cero.")
        valido = 0
    return valido
 
 
# ============================================================
# FUNCIONES DE CARGA DE BILLETES
# ============================================================
 
def cargar_billetes():
    lista_billetes = []
 
    print("Ingrese los billetes disponibles uno a uno.")
    print("Escriba -1 para terminar.")
 
    entrada = int(input("Billete: "))
 
    while entrada != -1 or lista_vacia(lista_billetes) == 1:
 
        if entrada == -1:
            entrada = int(input("Billete: "))
 
        elif lista_llena(lista_billetes) == 1:
            entrada = int(input("Billete: "))
 
        elif billete_en_rango(entrada) == 0:
            entrada = int(input("Billete: "))
 
        elif billete_repetido(entrada, lista_billetes) == 1:
            entrada = int(input("Billete: "))
 
        else:
            lista_billetes.append(entrada)
            print("Billete $" + str(entrada) + " agregado. " +
                  "Total ingresados: " + str(len(lista_billetes)))
            entrada = int(input("Billete: "))
 
    return lista_billetes
 
 
# ============================================================
# FUNCIONES DE ORDENAMIENTO
# ============================================================
 
def ordenar_mayor_a_menor(lista):
    copia = []
    i = 0
    while i < len(lista):
        copia.append(lista[i])
        i += 1
 
    n = len(copia)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if copia[j] < copia[j + 1]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
            j += 1
        i += 1
    return copia
 
 
def ordenar_operaciones_mayor_a_menor(operaciones):
    copia = []
    i = 0
    while i < len(operaciones):
        copia.append(operaciones[i])
        i += 1
 
    n = len(copia)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if copia[j][0] < copia[j + 1][0]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
            j += 1
        i += 1
    return copia
 
 
# ============================================================
# FUNCIONES DE CALCULO DEL MONTO
# ============================================================
 
def calcular_billetes_para_monto(monto, billetes_ordenados):
    resultado = []
    resto     = monto
    i         = 0
 
    while i < len(billetes_ordenados) and resto > 0:
        billete  = billetes_ordenados[i]
        cantidad = resto // billete
        if cantidad > 0:
            resultado.append([billete, cantidad])
            resto = resto - (billete * cantidad)
        i += 1
 
    if resto != 0:
        resultado = []
 
    return resultado
 
 
# ============================================================
# FUNCIONES DE PRESENTACION
# ============================================================
 
def mostrar_billetes(lista_billetes):
    print("\nBilletes disponibles: ", end="")
    i = 0
    while i < len(lista_billetes):
        print("$" + str(lista_billetes[i]), end="")
        if i < len(lista_billetes) - 1:
            print(", ", end="")
        i += 1
    print()
 
 
def mostrar_resultado_monto(monto, resultado):
    print("\nMonto $" + str(monto) + ":")
    i = 0
    while i < len(resultado):
        billete  = resultado[i][0]
        cantidad = resultado[i][1]
        print("  $" + str(billete) + " x " + str(cantidad) +
              " = $" + str(billete * cantidad))
        i += 1
 
 
def mostrar_resumen_operaciones(operaciones):
    if len(operaciones) == 0:
        print("\nNo se realizo ninguna operacion.")
 
    if len(operaciones) > 0:
        operaciones_ordenadas = ordenar_operaciones_mayor_a_menor(operaciones)
 
        print("\nRESUMEN DE OPERACIONES")
 
        i = 0
        while i < len(operaciones_ordenadas):
            monto     = operaciones_ordenadas[i][0]
            resultado = operaciones_ordenadas[i][1]
            print("\nMonto entregado: $" + str(monto))
            j = 0
            while j < len(resultado):
                billete  = resultado[j][0]
                cantidad = resultado[j][1]
                print("  $" + str(billete) + " x " + str(cantidad))
                j += 1
            i += 1
 
 
# ============================================================
# FUNCION PRINCIPAL
# ============================================================
 
def main():
 
    print("CAJERO AUTOMATICO")
 
    lista_billetes     = cargar_billetes()
    billetes_ordenados = ordenar_mayor_a_menor(lista_billetes)
    mostrar_billetes(billetes_ordenados)
 
    operaciones = []
 
    print("\nIngrese los montos a entregar.")
    print("Escriba -1 para terminar y ver el resumen.")
 
    monto = int(input("\nMonto: "))
 
    while monto != -1:
 
        if monto_valido(monto) == 1:
            resultado = calcular_billetes_para_monto(monto, billetes_ordenados)
 
            if len(resultado) == 0:
                print("Error: no es posible entregar $" + str(monto) +
                      " con los billetes disponibles.")
 
            if len(resultado) > 0:
                mostrar_resultado_monto(monto, resultado)
                operaciones.append([monto, resultado])
 
        monto = int(input("\nMonto: "))
 
    mostrar_resumen_operaciones(operaciones)
 
 
main()