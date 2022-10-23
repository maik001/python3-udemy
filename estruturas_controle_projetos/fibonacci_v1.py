# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci():
    # cria os dois primeiros números da sequência de fibonacci
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}',  end=',')
    # cria o loop infinito
    while True:
        # o próximo número recebe a soma do penultimo com o ultimo
        proximo = penultimo + ultimo
        print(proximo, end=',')
        # o ultimo agora é o penultimo
        penultimo = ultimo
        # e o proximo agora é o ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci()