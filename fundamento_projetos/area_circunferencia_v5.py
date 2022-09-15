# Usando o Módulo math para obter o valor de pi
from math import pi

raio = float(input('Digite um valor para o raio:'))
area_circunferencia = float(pi * raio ** 2)
print('A área do circulo é: ', area_circunferencia)
print('Nome do módulo: ', __name__)
print('Nome do pacote: ', __package__)
