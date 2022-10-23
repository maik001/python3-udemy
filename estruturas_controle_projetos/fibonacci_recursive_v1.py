# 0, 1, 1, 2, 3, 5, 8, 13, 21...
# valores padrão de argumentos -> tupla (0, 1)
def fibonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) < quantidade:
        # para ser considerado tupla, é necessária uma vírgula nos parênteses
        proximo = (sum(sequencia[-2:]),)
        sequencia += proximo
        # retorna a própria função que vai ser chamada recursivamente
        return fibonacci(quantidade, sequencia)
    return sequencia


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequência
    resultados = fibonacci(20)
    for fib in resultados:
        print(fib)
