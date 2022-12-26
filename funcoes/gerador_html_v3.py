# O parâmetro classe na função tag_bloco é opcional
def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*items):
    # join -> concatena os elementos de uma lista em uma string
    lista = ''.join(f'<li>{item}</li>' for item in items)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('Bloco', 'info', True))

    print(tag_bloco('Bloco', inline=True, classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2', 'Item 3', 'Item 4'), classe='info'))
