EDAD_MINIMA = 18

cant_personas = int(input('Ingresá una cantidad de personas: '))
cant_personas_mayores = 0

if cant_personas > 0:
    for cont_personas in range( cant_personas ):
        print('Ingresá la edad de la persona ', cont_personas + 1)
        edad = int(input())
        if edad >= EDAD_MINIMA:
            cant_personas_mayores += 1
else:
    print('La cantidad de personas no pueden ser menores a 0, lógico crack')

porcentaje = (cant_personas_mayores / cant_personas) * 100
print('El porcentaje de personas mayores de edad es de: ', porcentaje)


