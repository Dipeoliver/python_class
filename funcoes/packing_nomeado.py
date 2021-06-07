# **kwargs
# chamada de varios parametro para a função f1,
# faz o packing e coloca tudo dentro de um dicionario

def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f' {posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='Diego',
                 segundo='mario',
                 terceiro='dunha')
