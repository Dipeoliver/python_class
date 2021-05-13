from  math import pi
import sys
from typing import SupportsAbs

# função que recebe raio como parametro 


def circulo(raio):
    return round(pi * float(raio)**2,2)

# esta versão esta sem validacao

if __name__ == '__main__':
    sys.argv[1]=1   
    raio = sys.argv[1]
    area = circulo(raio) #passo o valor do raio como parametro e recebo o valor da função colocando em area
    print(area)


