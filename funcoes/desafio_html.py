def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        # ira verificar se contem html_classs e substituir por class
        kwargs['class'] = kwargs.pop('html_class')

    attrs = ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}<\{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python3, por'),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', 'e'),
            tag('strong', 'Diego Oliveira', id='do'),
            tag('span', '.'),
            html_class='alert')
    )
