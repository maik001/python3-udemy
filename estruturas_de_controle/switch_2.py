from random import randint


def get_dia_semana(dia_semana):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado'
    }
    dia_final = dias.get(dia_semana, f'{dia_semana} Não é um dia válido!')

    if dia_final in ('Sábado', 'Domingo'):
        return f'{dia_final} É um final de semana'
    elif dia_final in ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'):
        return f'{dia_final} É um dia da semana'
    else:
        return dia_final


if __name__ == '__main__':
    dia = randint(1, 7)
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')
