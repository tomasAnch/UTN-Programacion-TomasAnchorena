num = int(input('Ingresá un número entre 1 y 10: '))
if num > 0 and num <= 10:
    for c in range(1, 11):
        print( num, 'x', c, '=', (num * c) )
else: 
    print('Un número del 1 al 10 dije, tosco')
