def tag_bloco(conteudo, *args, classe='success', inline=False,**novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **novos_atrs)
    return f'<{tag} class="{classe}">{html}<\{tag}>'


def tag_lista(*itens, **novos_atrs):
    list = ''.join(f'<li>{item}<\li>' for item in itens)
    return f'<ul>{list}<\lu>'


if __name__ == '__main__':
    # print(tag_lista('casa', 'carro', 'familia'))
    # print(tag_bloco(tag_lista('casa', 'carro', 'familia'), inline=True))
    # print(tag_bloco(tag_lista('casa', 'carro', 'familia'), 'info'))

    # print(tag_bloco(tag_lista, 'sabado', 'Domingo', classe='info', inline=True))
    print(tag_bloco(tag_lista,'item1','Item2',classe='info',
                    bloco_accesskey='m',bloco_id ='conteudo', ul_id='lista'   ))
