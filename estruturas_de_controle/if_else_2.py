def faixa_etaria(idade):
    # verificar se os valores estão dentro do range passado
    if 0 <= idade < 18:
        return "Menor de Idade"
    elif idade in range(18, 65):
        return "Maturidade"
    elif idade in range(65, 100):
        return "Melhor idade"
    elif idade >= 100:
        return "Centenário"
    else:
        return "Idade inválida"


if __name__ == '__main__':
    # cria a tupla com os valores das idades
    for idade in (17, 0, 35, 87, 113, -2):
        # interpola com a fstring a função da faixa etária
        print(f'{idade}: {faixa_etaria(idade)}')