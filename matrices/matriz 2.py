def sumarmatrices(matriz1, matriz2):
    # Verificar si las matrices tienen las mismas dimensiones
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return None  # Las matrices no tienen las mismas dimensiones, no se pueden sumar
    # Obtener el número de filas y columnas de las matrices
    filas = len(matriz1)
    columnas = len(matriz1[0])
    # Crear una matriz para almacenar la suma
    suma = []
    # Iterar a través de las filas y columnas y sumar los elementos correspondientes
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(matriz1[i][j] + matriz2[i][j])
        suma.append(fila)
    return suma
# Ejemplo de uso
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
resultado = sumarmatrices(matriz1, matriz2)
if resultado:
    for fila in resultado:
        print(fila)
else:
    print("Las matrices no tienen las mismas dimensiones, no se pueden sumar.")






