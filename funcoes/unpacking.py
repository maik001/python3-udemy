def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma

if __name__ == '__main__':
    # packing - empacota os valores dentro da tupla e passa para a função
    print(soma_2(5, 10))
    print(soma_3(10, 10, 10))
    print(soma_n(100, 100))
    print(soma_n(10, 20, 30, 40, 50))

    # unpacking - desempacota a tupla, e passa os valores como parâmetros da função
    nums_tuple = (1, 2, 3, 4)
    print(soma_n(*nums_tuple))

    # unpacking -  desempacota a lista, e passa os valores como parâmetros da função
    nums_list = [1, 2, 3, 4]
    print(soma_n(*nums_list))
