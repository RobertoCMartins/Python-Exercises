
'''Ler a distância total(em km) percorrida por um carro, calcular o total de combustível gasto para  percorrer essa distância. 
O programa deve mostrar o consumo médio do carro, com duas casas decimais.'''

distancia: int
combustivelGasto: float; consumoMedioPorKM: float

distancia = int(input("Informe a distancia percorrida: "))
combustivelGasto = float(input("Informe a quantidade de combustivel gasto em litros: "))

consumoMedioPorKM = distancia/combustivelGasto

print(f"Consumo medio = {consumoMedioPorKM:.2f} KM por litro de combustível")