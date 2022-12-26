# O parâmetro classe na função tag_bloco é um parâmetro opcional
def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (assertions)
    # assert verifica se a saída de uma função é exatamente igual à um determinado valor passado
    assert tag_bloco('Incluido com Sucesso!') ==\
        '<div class="success">Incluido com Sucesso!</div>'
    assert tag_bloco('Impossível excluir!', 'error') == \
        '<div class="error">Impossível excluir!</div>'

    print(tag_bloco('Bloco'))


