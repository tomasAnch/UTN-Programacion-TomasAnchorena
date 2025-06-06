# def repetir_frase(num, frase):
#     if num >= 1:
#         print(frase)
#         repetir_frase( num - 1, frase)

# (repetir_frase(3, "Hola"))


# def suma_recursiva(num):
#     if num == 0:
#         return 0
#     else: 
#         return num + suma_recursiva( num - 1 )
    
# print(suma_recursiva(5))

def fibonacci_recursivo(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 2) + fibonacci_recursivo(pos - 1)
    
print(fibonacci_recursivo(6))