def triangulo_rectangulo(n):
  for i in range(1, n + 1):
    print("*" * i)
if __name__ == "__main__":
  n = int(input("Ingrese el número de filas: "))
  triangulo_rectangulo(n)