'''Fazer um programa para ler uma duração de tempo em segundos, imprimir esta duração no
   formato horas:minutos:segundos.
'''

duracaoSegundos = int; minutos = int; horas = int; resto = int

duracaoSegundos = int(input('Informe a duração em segundo: '))

horas = int(duracaoSegundos / 3600)
resto = duracaoSegundos % (60 * 60)

minutos = int(resto / 60)
resto = resto % 60

print(f'{horas}:{minutos}:{duracaoSegundos}')

