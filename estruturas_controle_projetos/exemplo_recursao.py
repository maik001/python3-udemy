def imprimir(maximo, atual):
    # condição de parada
    if atual < maximo:
        print(atual)
        # chama o método recursivamente, modificando um dos valores passados
        imprimir(maximo, atual + 1)

imprimir(10, 1)
