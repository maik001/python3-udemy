# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade):
    # cria a lista com os valores de início da sequência
    resultado = [0, 1]
    # enquanto o ultimo valor da lista dos resultados for menor que o limite
    while len(resultado) < quantidade:
        # adicionar na lista a soma do penultimo até último valor
        resultado.append(sum(resultado[-2:]))

    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequência
    resultados = fibonacci(20)
    for fib in resultados:
        print(fib)
