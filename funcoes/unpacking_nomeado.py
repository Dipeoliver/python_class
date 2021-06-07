# **kwargs
# pegando o dicionario e desempacotando ele com parametro para uma funcao

def resultado_f1(primeiro, segundo, terceiro):
    print(f' 1) {primeiro}')
    print(f' 1) {segundo}')
    print(f' 1) {terceiro}')


if __name__ == '__main__':
    podium = {'segundo': 'Diego', 'primeiro': 'Mario', 'terceiro': 'ze'}
    resultado_f1(**podium)
