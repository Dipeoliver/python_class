from  math import pi

# função que recebe raio como parametro 
def circulo(raio):
    return round(pi * float(raio)**2,2)


if __name__ == '__main__':
    raio = input('Informe o valor do Raio: ') # retorna uma string
    area = circulo(raio) #passo o valor do raio como parametro e recebo o valor da função colocando em area
    print(area)


