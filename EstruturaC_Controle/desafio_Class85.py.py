# constantes usar letra maiuscula

PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')
textos = ['Joao gosta de futebol e politica',
          'A praia foi divetida',
          ]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palvra proibida:', palavra)
            break
    else:
        print('Texto autorizado:', texto)
