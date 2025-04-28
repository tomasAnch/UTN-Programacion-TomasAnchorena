# Trabajo Práctico N°5 

#Objetivo:
#Desarrollar la comprensión y la capacidad de manipular listas en Python
#mediante la aplicación de conceptos fundamentales como la indexación, la
#modificación de elementos, el uso de métodos integrados y el manejo de
#listas anidadas.

#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

# array_numeros = list(range(4, 101, 4))
# print(array_numeros)


#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#   penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#   indexing con números negativos!

# array_cinco_elementos = [ 'Este', 'es', 'mi', 'trabajo', 'práctico' ]
# anteultimo_elemento_casero = array_cinco_elementos[3]
# print(anteultimo_elemento_casero)

# anteultimo_elemento_google = array_cinco_elementos[-2]
# print(anteultimo_elemento_google)


#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#   pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.

# array_vacio = []
# print(array_vacio)

# array_vacio.append('una palabra')
# array_vacio.append('otra palabra')
# array_vacio.append('golazo de mastantuono')
# print(array_vacio)


#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#   respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#   en los videos o bien investigar cómo funciona el indexing con números negativos!

# animales = ["perro", "gato", "conejo", "pez"]
# print(animales)

# animales[1] = "loro"
# animales[-1] = "oso"

# print(animales)


#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)

# Lo que se hace acá es remover del array el número más grande de los 5, la funcion máx asumo yo busca el nro. más grande en una lista.
# Luego el remove saca ese elemento del array.


#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#   pantalla los dos primeros.

# array_5_en_5 = list(range(10, 31, 5))
# print(array_5_en_5[0])
# print(array_5_en_5[1])

# print(array_5_en_5[:2])


#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera

# autos = ["sedan", "polo", "suran", "gol"]
# print(autos)

# autos[1] = 'renault'
# autos[2] = 'fitito'

# print(autos)


#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#   directamente. Imprimir la lista resultante por pantalla.

# dobles = []
# dobles.append(5 * 2)
# dobles.append(10 * 2)
# dobles.append(15 * 2)

# print(dobles)


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#   diferentes clientes:

# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# #a) Agregar "jugo" a la lista del tercer cliente usando append.
# compras[2].append("jugo")

# #b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# compras[1][1] = "tallarines"

# #c) Eliminar "pan" de la lista del primer cliente.
# compras[0].remove(compras[0][0])

# #d) Imprimir la lista resultante por pantalla
# print(compras)


#10)Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#   ● Posición lista_anidada[0]: 15
#   ● Posición lista_anidada[1]: True
#   ● Posición lista_anidada[2][0]: 25.5
#   ● Posición lista_anidada[2][1]: 57.9
#   ● Posición lista_anidada[2][2]: 30.6
#   ● Posición lista_anidada[3]: False
#   Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)










