cant_numeros = 5
sumatoria = 0

for cont in range(1, cant_numeros + 1):
    print('Ingresá un número', cont)
    num = int(input())
    sumatoria = sumatoria + num

print('La sumatoria de los valores es: ', sumatoria)
print('El valor promedio es: ', ( sumatoria / cant_numeros ))