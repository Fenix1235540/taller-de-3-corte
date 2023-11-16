letra = input("Introduce una letra: ")
codigoascii = ord(letra)
if (codigoascii >= 97 and codigoascii <= 122) or (codigoascii >= 65 and codigoascii <= 90):
    print("La letra es de abecedario.")
else:
    print("La letra no es de abecedario.")