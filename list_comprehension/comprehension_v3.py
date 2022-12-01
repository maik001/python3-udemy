# geração sob demanda de dados com generator
generator = (i ** 2 for i in range(10) if i % 2 == 0)

print(next(generator)) # Saída 0
print(next(generator)) # Saída 4
print(next(generator)) # Saída 16
print(next(generator)) # Saída 36
print(next(generator)) # Saída 64