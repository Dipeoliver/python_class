from  math import pi

# pegar valores atraves da entrada do teclado

if __name__ == '__main__':
    raius = input('Informe o valor do Raio: ') # retorna uma string
    print('Area do circulo',  round(pi * float(raius)**2,2))



