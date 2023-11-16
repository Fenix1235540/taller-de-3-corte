def es_primo(n):
  """Devuelve True si n es un número primo, False en caso contrario."""

  if n <= 1:
    return False

  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False

  return True


def imprimir_primos(n):
  """Imprime los números primos hasta n."""

  for i in range(2, n + 1):
    if es_primo(i):
      print(i)


if __name__ == "__main__":
  n = int(input("Ingrese un número: "))
  imprimir_primos(n)
