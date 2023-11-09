import math
def calcularnorma(vector):
    sumacuadrados = 0

    for elemento in vector:
        sumacuadrados += elemento ** 2

    norma = math.sqrt(sumacuadrados)

    return norma

# Ejemplo de uso
vector = [3, 4]  # Un vector de ejemplo
norma = calcularnorma(vector)
print(f"La norma del vector {vector} es {norma}")




