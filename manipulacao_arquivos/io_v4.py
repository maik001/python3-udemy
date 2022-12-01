arquivo = open('pessoas.csv')

# coloca-se no try trechos de código que podem gerar problemas
try:
    for registro in arquivo:
        # strip retira espaços em branco nas extremidades de uma String
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

# no finally trechos de código que devem ser sempre executados independentemente de erros
finally:
    print('finalmente')
    arquivo.close()

if arquivo.closed:
    print('O arquivo foi fechado')
