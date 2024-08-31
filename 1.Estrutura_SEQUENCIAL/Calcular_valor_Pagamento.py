'''Fazer um programa para ler:
- Nome de um(a) funcionário(a), 
- Valor que ele(a) recebe por hora
- Quantidade de horas trabalhadas por ele(a). 
- Mostrar o valor do pagamento do funcionário 
''' 

nomeFuncionario: str
valor: float; pagamento: float
horas: int

nomeFuncionario = str(input("Nome: "))
valor = float(input("Valor por hora: "))
horas = int(input("Horas trabalhadas: "))

pagamento = valor * horas

print(f"O pagamento para {nomeFuncionario} deve ser {pagamento:.2f}")