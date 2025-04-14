# cant_numeros = 5
# max = float('-inf')

# for cont in range( cant_numeros ):
#     print('Ingresá un número ', ( cont + 1 ))
#     num = int(input())
#     if num >= max:
#         max = num

# print('El número máximo fue: ', max)

##########################################################

# cant_numeros = 5
# min = float('inf')

# for cont in range( cant_numeros ):
#     print('Ingresá un número ', ( cont + 1 ))
#     num = int(input())
#     if num < min:
#         min = num

# print('El número mínimo fue: ', min)

##########################################################

cant_numeros = 5
print('Ingresá número 1')
num = int(input())

max = num
min = num
pos_max = -1
pos_min = -1

for cont in range( 2, cant_numeros + 1 ):
    print('Ingresá un número ', ( cont ))
    num = int(input())
    if num > max:
        max = num
        pos_max = cont
    elif num < min:
        min = num
        pos_min = cont

print('El número máximo fue: ', max, ' y salió en la posición ', pos_max)
print('El número mínimo fue: ', min, ' y salió en la posición ', pos_min)