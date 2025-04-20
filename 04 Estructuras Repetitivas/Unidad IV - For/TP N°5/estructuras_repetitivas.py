#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range(101):
#   print(i)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene

# print('Ingresá un número')
# num = (input())
# digitos = len(num)

# print(f'El número { num } tiene { digitos } dígitos') 
#La verdadverdad no tenía mucha idea de como hacer esto con un for, pensé en una variable digitos a la que
#podría sumarle los digitos haciendo el += pero no encontré la manera, me quise apoyar en la ia pero no me ayudó
#mucho que digamos, hacía un montón de código y no lograba lo que yo quería.


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

# print('Ingresá 2 números')
# num1 = int(input('1. '))
# num2 = int(input('2. '))
# max = 0
# min = 0

# if num1 < num2:
#   max = num2
#   min = num1
# else: 
#   max = num1
#   min = num2

# suma = 0

# for i in range(min + 1, max):
#   suma += i
  
# print( f'La suma entre { min } y { max } es: { suma }' )


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

# TIME_OUT = 0

# num = int(input('Ingresá un número'))
# suma = 0

# while num != TIME_OUT:
#   suma += num
#   num = int(input('Ingresá un número: '))

# print('La suma acumulada terminó siendo: ', suma)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random
# num_random = random.randint(0, 9)
# intentos = 0
# num_usuario = -1

# print('Adiviná un número entre 0 y 9!')

# while num_usuario != num_random:
#     num_usuario = int(input())
#     intentos += 1
#     if num_usuario != num_random:
#         print('Seguí participando jaj')

# print(f'Buenísimo!! Te tomó { intentos } intentos llegar al número random')


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for num in range(101, -1, -1): 
#   if num % 2 == 0:
#     print(num)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario

# print('Ingresá un número para calcular la suma desde 0')
# num = int(input())

# if num < 0:
#     print('Tiene que ser un número positivo fiera')
# else:
#     suma = 0
#     for i in range(0, num + 1):
#         suma += i

# print(f'La suma entre 0 y { num } es { suma }')


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# FIN = 5

# contador = 0
# par = 0
# impar = 0
# pos = 0
# neg = 0

# while contador < FIN:
#     print('Ingresá 100 numeritos!!')
#     numeros = int(input())

#     if numeros > 0:
#         pos += 1
#     else: 
#         neg += 1

#     if numeros % 2 == 0:
#         par += 1
#     else: 
#         impar += 1

#     contador += 1

# print(f'De estos 5 numeros habían { pos } positivos, { neg } negativos, { par } pares y { impar } impares')


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# FIN = 5
# contador = 0
# suma = 0

# print('Que onda fieraAA escribí 5 números para calcular su media!!')

# while contador < FIN:
#     print(f'Número { contador + 1 }')
#     num = int(input())
#     suma += num
#     contador += 1

# media = suma / FIN

# print(f'La media de estos { FIN } valores es { media }')


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print('Escribí un número para darlo vuelta!!')
num = int(input())

if num < 0:
  print('Un número positivo eraa')
else: 
  num_invertido = '' 

  while num > 0:
    ultimo_digito = num % 10
    num_invertido += str(ultimo_digito)
    num = num // 10

print(f'El número { num } invertido queda { num_invertido }')

