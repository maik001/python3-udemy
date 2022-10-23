# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(limite):
    # cria os dois primeiros números da sequência de fibonacci
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}',  end=',')
    # quando o último for menor que o limite a iteração é parada
    while ultimo < limite:
        # utilizando o packing para resumir a troca(swap) de valores das variáveis
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=',')


if __name__ == '__main__':
    fibonacci(100)
