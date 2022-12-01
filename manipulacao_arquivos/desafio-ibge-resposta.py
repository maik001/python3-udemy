#!usr/local/bin/python3
import csv
from urllib import request


def read(url):
    # abrindo a url com a declarativa with
    with request.urlopen(url) as entrada:
        print('Carregando arquivo CSV...')
        # mudando o enconding do arquivo da url passada
        dados = entrada.read().decode('latin1')
        print('Carregado com Sucesso')

        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    # lendo a url de forma literal com o "r" antes da string
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')