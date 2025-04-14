sueldo_anual = 0
cont_meses = 1

print('Ingresá tu sueldo para el mes n°', cont_meses)
sueldo_mensual = float(input())
while cont_meses < 12 and sueldo_mensual > 0:
    sueldo_anual += sueldo_mensual
    cont_meses += 1
    print('Ingresá tu sueldo del mes n°', cont_meses)
    sueldo_mensual = float(input())

if sueldo_mensual > 0:
    sueldo_anual += sueldo_mensual

print('Tu sueldo anual es:', sueldo_anual)