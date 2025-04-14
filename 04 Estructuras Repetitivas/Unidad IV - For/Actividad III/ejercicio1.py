num = int(input('Ingresá un número: '))

if num > 0:
    if num % 2 != 0:
        num -= 1
    cont = num
    while cont >= 0:
        print( str(cont) + ' ', end = '' )
        cont -= 2
else: 
    print('El número debe ser positivo')