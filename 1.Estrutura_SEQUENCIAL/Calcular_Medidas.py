
'''Fazer um programa para ler três medidas A, B e C. 
Em seguida, calcular e mostrar (imprimir os dados com quatro casas decimais):
- a) a área do quadrado que tem lado A
- b) a área do triângulo retângulo que base A e altura B
- c) a área do trapézio que tem bases A e B, e altura C'''

a = float; b = float; c = float; areaQuadrado= float; areaTrianguloRetangulo = float; areaTrapezio = float

a = float(input("Informa a media A: "))
b = float(input("Informa a media B: "))
c = float(input("Informa a media C: "))

areaQuadrado = a * a 
areaTrianguloRetangulo = (a * b) / 2
areaTrapezio = ((a * b ) *c) /2

print(f'A área do quadrado que tem o lado A é = {areaQuadrado:.4f}')
print(f'A área do triângulo retângulo que base A e altura B é = {areaTrianguloRetangulo:.4f}')
print(f'A área do trapézio que tem bases A e B, e altura C é = {areaTrapezio:.4f}')

