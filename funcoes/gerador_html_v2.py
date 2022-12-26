# O parâmetro classe na função tag_bloco é opcional
def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('Bloco', 'info', True))

    # Como eu alterei a ordem dos parâmetros, eu preciso dizer que
    # o argumento no qual eu estou me referindo
    print(tag_bloco('Bloco', inline=True, classe='error'))


