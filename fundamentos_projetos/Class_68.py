from  math import pi
import sys

# função que recebe raio como parametro 


def circulo(raio):
    return round(pi * float(raio)**2,2)

def help():
    print(f'''\
            É necessário informar a area do circulo
            Sintaxe: {sys.argv[0]} <area>''')

if __name__ == '__main__':
    if len(sys.argv) < 2:    
        help()    
    else :
        raio = sys.argv[1]
        area = circulo(raio) #passo o valor do raio como parametro e recebo o valor da função colocando em area
        print(area)


