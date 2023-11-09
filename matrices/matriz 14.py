def matrizidentidad(n):
    if n <= 0:
        return "El tamaño de la matriz debe ser un número positivo."
    # Inicializamos una matriz vacía
    matriz = []
    # Creamos la matriz identidad
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

# Ejemplo de uso
n = 4
mimatriz = matrizidentidad(n)





