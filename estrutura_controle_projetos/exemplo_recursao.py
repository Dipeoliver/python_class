# chamda recursiva, função que chama a si propio

def imprimir(maximo, atual):
    if atual >= maximo:
        return
    print(atual)
    imprimir(maximo, atual+1)


imprimir(10, 1)

print('------FIM-------')


def imprimir2(maximo, atual):
    # condicao de parada!
    if atual < maximo:
        print(atual)
    imprimir2(maximo, atual+1)


imprimir2(1000, 1)
