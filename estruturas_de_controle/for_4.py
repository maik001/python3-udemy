# for i in range(1, 10):
#     if i == 6:
#         break
#     print(i)
# else:
#     print("Fim")

from random import randint


def sortear_dado():
    return randint(1, 6)


for j in range(1, 7):
    valor_sorteio = sortear_dado()
    print(f'valor do índice: {j}, valor sorteado: {valor_sorteio}')
    if valor_sorteio % 2 != 0:
        continue
    if valor_sorteio % 2 == 0 and valor_sorteio == j:
        print('ACERTOU! :)')
        break
    else:
        print('NÃO ACERTOU! :(')
