# Percorrendo uma string
palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end='-')

# Percorrendo uma lista
aprovados = ['Matheus', 'Carlos', 'Maria', 'Rafael']
for nomes in aprovados:
    print(f'Um dos aprovados foi {nomes}')

# Separando a lista em índice -> valor
for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)

# Percorrendo uma Tupla
dias_semana = ('Domingo', 'Segunda', 'Terça,' 'Quarta',
               'Quinta', 'Sexta', 'Sábado')

for dias in dias_semana:
    print(f'Hoje é: {dias}')
