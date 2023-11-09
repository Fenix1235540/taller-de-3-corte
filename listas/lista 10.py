# Definir dos vectores como listas
vector1 = [1, 2, 3, 4]
vector2 = [5, 6, 7, 8]

# Verificar que los vectores tienen la misma longitud
if len(vector1) == len(vector2):
    # Inicializar una variable para el resultado del producto punto
    productopunto = 0
    
    # Iterar a través de los elementos de los vectores
    for i in range(len(vector1)):
        # Multiplicar los elementos correspondientes y sumar al resultado
        productopunto += vector1[i] * vector2[i]
    
    # Imprimir el resultado del producto punto
    print("El producto punto de los dos vectores es:", productopunto)
else:
    print("Los vectores tienen longitudes diferentes, no se puede calcular el producto punto.")




