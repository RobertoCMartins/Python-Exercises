# Calcular a Area, Perimetro e Diagonal de um Retangulo

#Importando módulo matemático
import math

base: float; altura: float; area: float; perimetro: float; diagonal: float

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = base * altura
perimetro = 2 * (base + altura)
# Raiz quadrada com o método math.sqrt
diagonal = math.sqrt(base * base + altura * altura)


print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.2f}")
print(f"DIAGONAL = {diagonal:.2f}")

