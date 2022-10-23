# 0, 1, 1, 2, 3, 5, 8, 13, 21...
# valores padrão de argumentos -> tupla (0, 1)
def fibonacci(quantidade, sequencia=(0, 1)):
    # reduzindo a quantidade de linhas com o operador ternário
    return sequencia if len(sequencia) == quantidade \
        else fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequência
    resultados = fibonacci(20)
    for fib in resultados:
        print(fib)
