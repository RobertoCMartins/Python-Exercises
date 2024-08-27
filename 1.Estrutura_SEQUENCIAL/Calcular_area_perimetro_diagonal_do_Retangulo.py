# Calcular a Area de um Retangulo

#Importando módulo matemático
import math

base: float; altura: float; area: float; perimetro: float; diagonal: float

base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))

area = base * altura
perimetro = 2 * (base + altura)
# Raiz quadrada com o método math.sqrt
diagonal = math.sqrt(base * base + altura * altura)


print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.2f}")
print(f"DIAGONAL = {diagonal:.2f}")

