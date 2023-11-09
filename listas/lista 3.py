# Lista de números
numeros = [2, 4, 6, 8, 10]

# Inicializar la suma total
suma = 0

# Contar la cantidad de elementos en la lista
contador = 0

# Iterar a través de la lista y sumar los valores
for numero in numeros:
    suma += numero
    contador += 1

# Calcular la media
media = suma / contador

print("La media es:", media)
