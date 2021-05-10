# lista e um estrutura indexada
lista = [1,5,'Diego','Mario', 3.1415]
print(lista.index('Diego'))   # identifica o index do item na lista
print(lista[2]) #imprimir uma posição da lista

print(1 in lista)  # verifica se 1 contem dentro da lisat
print(lista[-1]) # pegar a ultima posição da lista
print(lista[-5]) # pegar a primeira posição da lista

lista.append('Mario2') # insere intens no final da lista
lista.insert(4,"aoo") # inseri itens na lista em uma determinada posição
print(lista)


lista2 = ['CARRO', 'AVIAO','BARCO']
lista2.sort() # FAZ UM ALEATORIO DOS VALORES
print(lista2)