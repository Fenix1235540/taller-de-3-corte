def calculardeterminante(matriz):
    if len(matriz) != 2 or len(matriz[0]) != 2 or len(matriz[1]) != 2:
        raise ValueError("La matriz no es una matriz 2x2")
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]
    determinante = (a * d) - (b * c)
    return determinante

# Ejemplo de uso:
matriz = [[3, 5], [2, 7]]
det = calculardeterminante(matriz)
print("El determinante de la matriz es:", det)






