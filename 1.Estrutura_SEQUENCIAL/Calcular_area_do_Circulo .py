# Calcular a área do Círculo

# Importando função matemática para utilizar a constante que retorna o valor de PI
import math

raio: float; area: float
numeroPi = math.pi

raio = float(input("Digite o valor do raio do circulo: "))


# area = PI * raio ao quadrado (raio * raio)
area = numeroPi * raio * raio

print(f"Valor da ÁREA é = {area:.2f}")
