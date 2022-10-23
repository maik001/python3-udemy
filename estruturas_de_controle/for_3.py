produto = {'nome': 'Caneta Chic', 'preco': 14.99, 'importada': True, 'estoque': 793}

# pegando as chaves de um dicionário
for chave in produto:
    print(chave)

# pegando os valores de um dicionário
for valor in produto.values():
    print(valor)

# pegando as chave e valores dos itens do dicionário produto
for chave, valor in produto.items():
    print(chave, '->', valor)

# as variáveis chave e valor estão acessíveis no módulo main ou contexto global
print(chave, '->', valor)