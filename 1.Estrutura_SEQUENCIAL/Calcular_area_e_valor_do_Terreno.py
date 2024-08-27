# Calcular a Area em m2 de um terrerno quadrado ou retangular, e o valor desse terreno com base no preço do m2.

largura: float; 
comprimento: float; 
valor: float; 
areaM2: float; 
preco: float

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor = float(input("Digite o valor do metro quadrado: "))

areaM2 = largura * comprimento

# Valor formatado ":.2f" no caso de 2 casas decimais
print(f"Area do terreno = {areaM2:.2f}")

preco = areaM2 * valor

print(f"Preco do terreno = {preco:.2f}\n")
