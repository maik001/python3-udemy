#!usr/local/bin/python3
import csv

# abre o arquivo csv passado
with open('desafio-ibge.csv', encoding='ISO-8859-1') as arquivo:

    # abre o arquivo que será resultado da manipulação no modo escrita
    with open('desafio-ibge-result.csv', 'w') as saida:
        resultado = csv.writer(saida)
        print(f'Gerando Arquivo {saida.name}...')

        # pula o cabeçalho do arquivo csv
        next(arquivo)
        for linha in csv.reader(arquivo):
            linhaTotal = [linha[3], linha[8]]
            resultado.writerow(linhaTotal)

        print(f'Arquivo {saida.name} gerado com sucesso!')
