from funcion_laberinto import resolver_laberinto

laberinto = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0]  # Meta en (8, 7)
]

camino = []

resolver_laberinto( laberinto, 0, 0, camino )

print( camino )