def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def obtener_resto(num1, num2):
    return num1 - num2 * (num1 // num2)

def es_multiplo(x, y):
    return obtener_resto(x, y) == 0

def sumatoria_divisores_propios(numero):
    sumatoria = 0
    for i in range(1, numero // 2 + 1):
        if es_multiplo(numero, i):
            sumatoria += i
    return sumatoria
        
def es_perfecto(numero):
    return sumatoria_divisores_propios(numero) == numero

def informar_si_numero_es_perfecto(numero):
    if es_perfecto(numero):
        print(f"El numero {numero} es perfecto")
    else:
        print(f"El numero {numero} NO es perfecto")


num = leer_entero_validado("Ingrese un número natural", 1)
informar_si_numero_es_perfecto(num)