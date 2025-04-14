umbral = 10
sumatoria = 0
cont = 0

while sumatoria < umbral:
    cont += 1
    print('Ingrese un número', cont)
    num = int(input())
    sumatoria += num

print('El promedio de valores es: ', sumatoria / cont)