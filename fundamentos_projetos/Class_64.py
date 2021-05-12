from  math import pi

# função que recebe raio como parametro e nao retorna nada
def circulo(raio):
    print('Area do circulo',  round(pi * float(raio)**2,2))


if __name__ == '__main__':
    raio = input('Informe o valor do Raio: ') # retorna uma string
    circulo(raio) #passo o valor do raio como parametro


