# quando a declaração with abre um recurso, ao sair do bloco, ele sempre fecha o recurso
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        # strip retira espaços em branco nas extremidades de uma String
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('O arquivo foi fechado')
