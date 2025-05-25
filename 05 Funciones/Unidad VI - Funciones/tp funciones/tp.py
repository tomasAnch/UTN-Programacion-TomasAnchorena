#1 - Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal

# # FUNCIONES
# def imprimir_hola_mundo():
#     print('Hola Mundo!')

# # PROGRAMA PRINCIPAL
# imprimir_hola_mundo()

##############################################################################################################################################################

#2 - Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# # FUNCIONES
# def saludar_usuario(nombre):
#     print(f'Hola {nombre}!')

# # PROGRAMA PRINCIPAL
# nombre = input('Decime tu nombre ')
# saludar_usuario(nombre)

##############################################################################################################################################################

#3 - Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) 
# que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# # FUNCIONES
# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

# # PROGRAMA PRINCIPAL
# print('Te pido los datos maestro, un tramite')
# nombre = input('Decime tu nombre: ')
# apellido = input('Y apellido: ')
# edad = input('Edad?: ')
# residencia = input('Barbaro, ahora donde vivís y cerramos: ')

# informacion_personal(nombre, apellido, edad, residencia)

##############################################################################################################################################################

#4 - Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# import math

# pi = math.pi

# # FUNCIONES
# def calcular_area_circulo(radio):
#     area = pi * (radio**2)
#     print(f'El área de un círculo con radio {radio} es {area}')

# def calcular_perimetro_circulo(radio):
#     perimetro = 2 * pi * radio
#     print(f'El perimetro del círculo es {perimetro}')
    
# # PROGRAMA PRINCIPAL
# radio = int(input('Decime el radio del círculo: '))
# calcular_area_circulo(radio)
# calcular_perimetro_circulo(radio)

##############################################################################################################################################################

#5 - Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# # FUNCIONES
# def segundos_a_horas(segundos):
#     horas = segundos / 3600
#     print(f'{segundos} segundos equivalen a {horas} hora/s')

# # PROGRAMA PRINCIPAL
# segundos = int(input('Ingresá los segundos para calcular a cuantas horas equivalen: '))
# segundos_a_horas(segundos)

##############################################################################################################################################################

#6 - Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# # FUNCIONES
# def tabla_multiplicar(numero):
#     print(f'{numero} x 1')
#     print(f'{numero} x 2')
#     print(f'{numero} x 3')
#     print(f'{numero} x 4')
#     print(f'{numero} x 5')
#     print(f'{numero} x 6')
#     print(f'{numero} x 7')
#     print(f'{numero} x 8')
#     print(f'{numero} x 9')
#     print(f'{numero} x 10')

# # PROGRAMA PRINCIPAL
# numero = int(input('Ingresá un número para ver su tabla del 1 al 10: '))
# tabla_multiplicar(numero)

##############################################################################################################################################################

#7 - Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# # FUNCIONES
# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b

#     return (suma, resta, multiplicacion, division)

# # PROGRAMA PRINCIPAL
# a = int(input('Ingresá el primer número: '))
# b = int(input('Ingresá el segundo número: '))

# resultados = operaciones_basicas(a, b)

# suma, resta, multiplicacion, division = resultados

# print(f"Suma: {suma}")
# print(f"Resta: {resta}")
# print(f"Multiplicación: {multiplicacion}")
# print(f"División: {division}")

##############################################################################################################################################################

#8 - Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# # FUNCIONES
# def calcular_imc(peso, altura):
#     imc = peso / (altura ** 2)
#     print(f'El índice de masa corporal es {imc}')

# # PROGRAMA PRINCIPAL
# peso = int(input('Decime tu peso fiera: '))
# altura = float(input('Ahora la altura: '))
# calcular_imc(peso, altura)

##############################################################################################################################################################

#9 - Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# # FUNCIONES
# def celsius_a_fahrenheit(celsius):
#     fahrenheit = celsius * (9/5) + 32
#     print(f'{celsius} grados Celcius son {fahrenheit} Fahrenheit')

# # PROGRAMA PRINCIPAL
# print('Decime una temperatura en Celsius! ')
# celsius = int(input(''))
# celsius_a_fahrenheit(celsius)

##############################################################################################################################################################

#10 - Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

# FUNCIONES
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# PROGRAMA PRINCIPAL
a = int(input('Decime el primer número: '))
b = int(input('El segundo: '))
c = int(input('Y el tercero: '))

res_promedio = calcular_promedio(a, b, c)

print(f'El promedio de {a}, {b} y {c} es {res_promedio}')

















