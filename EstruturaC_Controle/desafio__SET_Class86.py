# constantes usar letra maiuscula

PALAVRAS_PROIBIDAS = {'futebol', 'religiao', 'politica'}
textos = ['Joao gosta de futebol e politica',
          'A praia foi divetida',
          ]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui pelo menos uma palvra proibida:', texto, intersecao)
    else:
        print('Texto autorizado:', texto)
