# Lista de números
numeros = [5, 10, 2, 8, 15, 3]

# Inicializa una variable para almacenar el número mayor
numero_mayor = numeros[0]

# Itera a través de la lista
for numero in numeros:
    if numero > numero_mayor:
        numero_mayor = numero

# El número mayor se almacenará en la variable 'numero_mayor'
print("El número mayor es:", numero_mayor)
