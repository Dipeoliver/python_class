from  math import pi
import sys

# função que recebe raio como parametro 


def circulo(raio):
    return round(pi * float(raio)**2,2)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('''\
            É necessário informar a area do circulo
            Sintaxe: area_circulo<area>''')
    else :
        raio = sys.argv[1]
        area = circulo(raio) #passo o valor do raio como parametro e recebo o valor da função colocando em area
        print(area)


