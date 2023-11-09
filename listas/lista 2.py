def encontrarnumeromenoryposicion(lista):
    if not lista:
        return None, None
    menor = lista[0]
    posicion = 0  
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            posicion = i
    return menor, posicion

milista = [12, 45, 3, 17, 6, 30, 8]
numeromenor, posicion = encontrarnumeromenoryposicion(milista)
print(f"El número menor es {numeromenor} y se encuentra en la posición {posicion}.")


