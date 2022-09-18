# Usando o Módulo math para obter o valor de pi
from math import pi
import sys

# o def é a palavra reservada na python para criar uma função
def calcular_area(raio):
    area_circunferencia = float(pi * raio ** 2)
    return area_circunferencia


# verifica se o módulo do python que eu estou é o main (principal)
if __name__ == '__main__':
    # pega o segundo argumento da execução do script no terminal e coloca na variável raio
    raio = float(sys.argv[1])
    area = calcular_area(raio)
    print('A área da circunferência é: ', area)
