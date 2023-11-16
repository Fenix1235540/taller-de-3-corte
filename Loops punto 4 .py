def floyd_triangle(n):
  """
  Imprime el Triángulo de Floyd de tamaño n.
  Args:
    n: El número de filas del triángulo.
  Returns:
    Ninguno.
  """
  triangle = []
def triangulo_rectangulo(n):
  """
  Imprime un patrón como un triángulo rectángulo con el número aumentado en 1.
  Args:
    n: La altura del triángulo.
  Returns:
    Nada.
  """
  for i in range(1, n + 1):
    for j in range(1, i + 1):
      print(j, end=" ")
    print()
if __name__ == "__main__":
  n = int(input("Ingrese la altura del triángulo: "))
  triangulo_rectangulo(n)