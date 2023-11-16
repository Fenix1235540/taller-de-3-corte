def es_vocal(caracter):
  """
  Verifica si el caracter ingresado es una vocal.
  Args:
    caracter: El caracter a verificar.
  Returns:
    True si el caracter es una vocal, False en caso contrario.
  """
  vocales = ["a", "e", "i", "o", "u"]
  return caracter in vocales
def main():
  """
  Programa principal.
  """
  caracter = input("Ingrese un caracter: ")
  caracter = caracter.lower()
  if es_vocal(caracter):
    print("El caracter {} es una vocal.".format(caracter))
  else:
    print("El caracter {} es una consonante.".format(caracter))
if __name__ == "__main__":
  main()