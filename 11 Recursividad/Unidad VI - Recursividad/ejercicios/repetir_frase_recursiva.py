def repetir_frase(num, frase):
    if num>=1:
        print(frase)
        repetir_frase(num - 1, frase)

if __name__ == "__main__":
    repetir_frase(3, 'freecs')