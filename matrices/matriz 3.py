def multiplicarmatrizporescalar(matriz, escalar):
    # Obtén las dimensiones de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])

    # Crea una matriz de ceros con las mismas dimensiones que la matriz original
    resultado = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Multiplica cada elemento de la matriz por el escalar
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = matriz[i][j] * escalar

    return resultado

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
escalar = 2
resultado = multiplicarmatrizporescalar(matriz, escalar)
print(resultado)





