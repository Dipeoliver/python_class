lista = ['ana','lia','rui','Paulo','Dani']
print(lista[1:3]) # acessando a partir do indice 1 ate o indice 2 o 3 nao entra

print(lista[1:-1])

print(lista[:]) # acessando a lista toda

print(lista[::2]) # acessando a lista de 2 em 2

del lista[2]
print(lista) # apagando uma posiçõa da lista

del lista[1:]
print(lista)