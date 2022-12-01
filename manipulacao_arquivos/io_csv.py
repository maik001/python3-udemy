# importação do módulo csv
import csv

with open('pessoas.csv') as entrada:
    # utiliza o módulo csv para ler o arquivo, fazendo todas as tratativas necessárias
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'. format(*pessoa))

