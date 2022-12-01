# quando a declaração with abre um recurso, ao sair do bloco, ele sempre fecha o recurso
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            # o file significa que o print vai escrever a saida dentro do arquivo especificado
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('O arquivo de pessoa foi fechado')

if saida.closed:
    print('O arquivo de saída foi fechado')