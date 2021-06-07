def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}<\div>'


if __name__ == '__main__':
    # Teste (assertion) teste para verificar se o resultado é verdadeiro
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!<\div>'
    assert tag_bloco('Impossivel excluir!', 'error') == \
        '<div class="error">Impossivel excluir!<\div>'

    print(tag_bloco('bloco'))
