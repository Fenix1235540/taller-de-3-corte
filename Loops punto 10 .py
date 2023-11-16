def mostrar_digitos(numero):
  """
  Muestra cada uno de los dígitos de un número.
  Args:
    numero: El número a mostrar los dígitos.
  Returns:
    Ninguno.
  """
  numero_list = list(str(numero))
  for digito in numero_list:
    print(digito)
if __name__ == "__main__":
  numero = input("Ingrese un número: ")
  mostrar_digitos(numero)