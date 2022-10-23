# laço infinito, "enquanto" verdade
# while True:
#     print('Vai demorar muuuuuuito')

# importando a função randint do módulo random, para a geração de valores aleatórios
from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

# A estrutura while é utilizada principalmente quando voce tem uma quantidade indeterminada de repetições
while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o número:'))

print(f'Número Secreto {numero_secreto} foi encontrado')
