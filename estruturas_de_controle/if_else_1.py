# 10.0 à 9.1 - A
# 9.0 à 8.1 - A-
# 8.0 à 7.1 - B
# 7.0 à 6.1 - B-
# 6.0 à 5.1 - C
# 5.0 à 4.1 - C-
# 4.0 à 3.1 - D
# 3.0 à 2.1 - D-
# 2.0 à 1.1 - E
# 1.0 À 0.0 - E-

# Para notas maiores que 10 e menores que 0, será impresso "Nota Inválida"
def converte_nota_conceito(nota):
    if nota > 10.0 or nota < 0.0:
        return 'Nota Inválida'
    elif nota > 9.0:
        return 'Você tirou um A'
    elif nota > 8.0:
        return 'Você tirou um A-'
    elif nota > 7.0:
        return 'Você tirou um B'
    elif nota > 6.0:
        return 'Você tirou um B-'
    elif nota > 5.0:
        return 'Você tirou um C'
    elif nota > 4.0:
        return 'Você tirou um C-'
    elif nota > 3.0:
        return 'Você tirou um D'
    elif nota > 2.0:
        return 'Você tirou um D-'
    elif nota > 1.0:
        return 'Você tirou um E'
    elif nota > 1.0:
        return 'Você tirou um E-'


if __name__ == '__main__':
    valor_nota = float(input('Digite a nota do aluno:'))
    resultado = converte_nota_conceito(valor_nota)

    print(resultado)
