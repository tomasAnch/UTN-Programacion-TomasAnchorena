# FUNCIONES
def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def imprimir_matriz(nro_columnas, nro_filas):
    for i in range(nro_filas):
        imprimir_simbolo("X", nro_columnas)

def imprimir_simbolo(simbolo, veces):
    print(sucesion_simbolos(simbolo, veces))

def sucesion_simbolos(simbolo, veces):
    sucesion = ""
    for i in range(veces):
        sucesion += simbolo
    return sucesion


# PROGRAMA 
ancho = leer_entero_validado('Ingresá el ancho', 1)
alto = leer_entero_validado('Ingresá el alto', 1)
imprimir_matriz(ancho, alto)




