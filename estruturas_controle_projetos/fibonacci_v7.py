# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade):
    # cria a lista com os valores de início da sequência
    resultado = [0, 1]
    # a notação _ é utilizada ao ter uma variável que não está em uso
    # começando o range a partir do segundo índice, até a quantidade passada da sequência
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequência
    resultados = fibonacci(20)
    for fib in resultados:
        print(fib)
