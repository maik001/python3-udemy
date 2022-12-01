arquivo = open('pessoas.csv')

for registro in arquivo:
    # strip retira espaços em branco nas extremidades de uma String
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()

