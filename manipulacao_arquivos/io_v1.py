# lê o arquivo na nossa máquina, a função open está no builtins
arquivo = open('pessoas.csv')

# armazena os dados do arquivo dentro de uma variável através do método read
dados = arquivo.read()

# após armazenar os dados do arquivo na variável podemos fechar o arquivo
# para liberar o recurso de memória que estava sendo usando
arquivo.close()

# percorre cada linha do arquivo
for registro in dados.splitlines():
    # split -> quebra o registro da linha separando por virgula
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
