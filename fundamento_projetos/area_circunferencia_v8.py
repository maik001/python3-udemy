# Usando o Módulo math para obter o valor de pi
from math import pi


# o def é a palavra reservada na python para criar uma função
def calcular_area(raio):
    area_circunferencia = float(pi * raio ** 2)
    return area_circunferencia


# verifica se o módulo do python que eu estou é o main (principal)
if __name__ == '__main__':
    raio = float(input('Digite um valor para o raio:'))
    area = calcular_area(raio)
    print('A área da circunferência é: ', area)
