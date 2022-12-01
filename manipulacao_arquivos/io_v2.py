arquivo = open('pessoas.csv')

# streaming de dados, pega-se somente a parte do arquivo/dado que interessa para o laço de repetição
# diferente da função read, que coloca os dados do arquivo para uma variável em memória
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')), end = '')

arquivo.close()

