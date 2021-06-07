def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}<\{tag}>'


if __name__ == '__main__':

    print(tag_bloco('bloco', 'Teste', True))
    print(tag_bloco('inline', inline=True))

    print(tag_bloco('bloco', classe='Teste'))
