from  math import pi

# pegar valores atraves da entrada do teclado


raius = input('Informe o valor do Raio: ') # retorna uma string
area = pi * float(raius)**2 

print('Area do circulo',  round(area,2))