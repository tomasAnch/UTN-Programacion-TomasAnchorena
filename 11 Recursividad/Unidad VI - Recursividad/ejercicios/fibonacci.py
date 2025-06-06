def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else: 
        return fibonacci( pos - 1 ) + fibonacci( pos - 2 )

if __name__ == "__main__":
    print(fibonacci(6))