def primeros_primos(n):
  """
  Devuelve una lista de los primeros (n) números primos.
  Args:
    n: El número de números primos a devolver.
  Returns:
    Una lista de números primos.
  """
  primos = []
  for i in range(2, n + 1):
    primo = True
    for j in range(2, int(i ** 0.5) + 1):
      if i % j == 0:
        primo = False
        break
    if primo:
      primos.append(i)
  return primos
def main():
  n = int(input("Introduzca el número de números primos a mostrar: "))
  primos = primeros_primos(n)
  print("Los primeros {} números primos son:".format(n))
  for primo in primos:
    print(primo)
if __name__ == "__main__":
  main()
