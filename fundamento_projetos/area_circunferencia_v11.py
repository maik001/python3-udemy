# Usando o Módulo math para obter o valor de pi
from math import pi
import sys


def ajuda():
    print(f'''\
    Você precisa inserir outro argumento para o raio.
    Padrão: {sys.argv[0]} <raio>''')


# o def é a palavra reservada na python para criar uma função
def calcular_area(raio):
    area_circunferencia = float(pi * raio ** 2)
    return area_circunferencia


# verifica se o módulo do python que eu estou é o main (principal)
if __name__ == '__main__':
    # validar se o número de argumentos passados é menor que 2
    if len(sys.argv) < 2:
        ajuda()
    else:
        raio = float(sys.argv[1])
        area = calcular_area(raio)
        print('A área da circunferência é: ', area)
