# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(limite):
    # cria a lista com os valores de início da sequência
    resultado = [0, 1]
    # enquanto o ultimo valor da lista dos resultados for menor que o limite
    while resultado[-1] < limite:
        # adicionar na lista a soma do penultimo até último valor
        resultado.append(sum(resultado[-2:]))

    return resultado


if __name__ == '__main__':
    resultados = fibonacci(100)
    for fib in resultados:
        print(fib)
