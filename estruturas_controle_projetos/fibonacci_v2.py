# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(limite):
    # cria os dois primeiros números da sequência de fibonacci
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}',  end=',')
    # quando o último for menor que o limite a iteração é parada
    while ultimo < limite:
        # o próximo número recebe a soma do penultimo com o ultimo
        proximo = penultimo + ultimo
        print(proximo, end=',')
        # o ultimo agora é o penultimo
        penultimo = ultimo
        # e o proximo agora é o ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci(80)
