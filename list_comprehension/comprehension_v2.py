# forma básica de conseguir o dobro somente dos pares de um intervalo
dobro_do_par = []
for i in range(10):
    if i % 2 == 0:
        dobro_do_par.append(i * 2)

print(dobro_do_par)


# [ expressão for item in list if condicional]
dobro_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]

print(dobro_dos_pares)