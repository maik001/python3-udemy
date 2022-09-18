# Usando o Módulo math para obter o valor de pi
from math import pi

# verifica se o módulo do python que eu estou é o main (principal)
if __name__ == '__main__':
    raio = float(input('Digite um valor para o raio:'))
    area_circunferencia = float(pi * raio ** 2)
    print('A área do circulo é: ', area_circunferencia)
