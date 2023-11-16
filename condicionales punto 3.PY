def esnegativo(n):
    return n < 0
def espositivo(n):
    return n > 0
def escero(n):
    return n == 0
n = float(input("Ingrese un número: "))
if esnegativo(n):
    print("El número es negativo.")
elif espositivo(n):
    print("El número es positivo.")
else:
    print("El número es cero.")