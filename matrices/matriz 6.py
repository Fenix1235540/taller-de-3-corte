def sumafilascolumnas(matriz):
    numfilas = len(matriz)
    numcolumnas = len(matriz[0])
    # Inicializar listas para almacenar las sumas de filas y columnas
    sumasfilas = [0] * numfilas
    sumascolumnas = [0] * numcolumnas
    # Calcular las sumas de las filas
    for i in range(numfilas):
        for j in range(numcolumnas):
            sumasfilas[i] += matriz[i][j]
    # Calcular las sumas de las columnas
    for j in range(numcolumnas):
        for i in range(numfilas):
            sumascolumnas[j] += matriz[i][j]
    return sumasfilas, sumascolumnas

# Ejemplo de uso
matrizejemplo = [  [1, 2, 3], [4, 5, 6],[7, 8, 9]]
sumasfilas, sumascolumnas = sumafilascolumnas(matrizejemplo)
print("Sumas de las filas:")
for i, suma in enumerate(sumasfilas):
    print(f"Fila {i + 1}: {suma}")
print("Sumas de las columnas:")
for j, suma in enumerate(sumascolumnas):
    print(f"Columna {j + 1}: {suma}")






