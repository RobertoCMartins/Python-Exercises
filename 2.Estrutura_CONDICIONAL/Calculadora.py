def calculadora():
  """Uma simples calculadora em Python."""

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  operacao = input("Digite a operação (+, -, *, /): ")

  if operacao == '+':
    resultado = num1 + num2
  elif operacao == '-':
    resultado = num1 - num2
  elif operacao == '*':
    resultado = num1 * num2
  elif operacao == '/':
    if num2 == 0: 

      print("Divisão por zero não é permitida.")
    else:
      resultado = num1 / num2
  else:
    print("Operação inválida.")

  if 'resultado' in locals():
    print("Resultado:", resultado)

calculadora()