CORTE = '*'
NOMBRE_INVALIDO = 'XXXXXXXXXXXXXXXXXXX'
edad_minima = float( "inf" )
nombre_del_mas_joven = NOMBRE_INVALIDO

nombre = input('Ingresá un nombre (' + CORTE + ' para cortar): ')
while nombre != CORTE:
    edad = int(input('Ingresá la edad de ' + nombre + ": "))
    if edad < edad_minima:
        edad_minima = edad
        nombre_del_mas_joven = nombre
    nombre = input('Ingresá otro nombre (' + CORTE + ' para cortar): ')

if nombre_del_mas_joven == NOMBRE_INVALIDO:
    print('No se ingresaron personas')
else:
    print('La persona más joven (', edad_minima,'años) es: ', nombre_del_mas_joven)





