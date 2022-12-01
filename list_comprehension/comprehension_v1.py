# forma básica de conseguir o dobro de um intervalo
dobro = []
for i in range(1, 11):
    dobro.append(i * 2)
print(dobro)


# [ expressão for item in list if condicional]
# utilizando o formato list comprehension
dobros = [i * 2 for i in range(1, 11)]
print(dobros)