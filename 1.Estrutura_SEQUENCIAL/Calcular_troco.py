# Calcular o valor do troco

preco: float; dinheiro: float; valorCompra: float; troco: float
qtd: int

preco = float(input("Informe o preço unitário do produto: "))
qtd = int(input("Digite a quantidade comprada: "))
dinheiro = float(input("Informe o valor recebido: "))

valorCompra = preco * qtd
troco = dinheiro - valorCompra

print(f"TROCO referente a compra no valor de R$ {valorCompra} é = R$ {troco:.2f}")
