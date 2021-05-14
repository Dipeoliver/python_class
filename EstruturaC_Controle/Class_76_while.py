# while True:
#     print('Vai demorar muito')

# para quantidade idefinida de dados usar while.

from random import randint

numero_informado = -1 # iniciou com zero porque se iniciar com zero poderia ser o primiero numero
numero_secreto = randint(0,9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe um numero: '))

print('O numero secreto é: ',numero_secreto)