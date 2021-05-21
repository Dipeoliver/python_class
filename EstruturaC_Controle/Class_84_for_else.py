# constantes usar letra maiuscula
from typing import Text


PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')
textos = ['Joao gosta de futebol e politica',
          'A praia foi divetida',
          ]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palvra proibida:', palavra)
            found = True
            break
    if not found:
        print('Texto autorizado:', texto)
