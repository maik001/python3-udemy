# Importando o decimal e o getcontext
from decimal import Decimal, getcontext

# definindo a precisão das casas decimais para 6
getcontext().prec = 6
pi = Decimal('3.14159')
raio = Decimal(input('Digite um valor para o raio:'))
area_circunferencia = Decimal(pi * raio ** 2)
print('A área do circulo é: ', area_circunferencia)
