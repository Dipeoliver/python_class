# SET não aceita valores duplicados
# valores de entrada são aleatorios
# nao aceita indice

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

setA.difference_update(setB) # diferença que A tem de B
print(setA)

A = {1,2,3,4,5,6}
B = {1,2,3}
C= {7,8,9}

print(B.issubset(A)) # O B contem no A

print(A.issubset(B))  # O A NÂO contem no B

print(A.isdisjoint(C)) # O C aceita  juntar com A ( nao contem itens iguais)

x = frozenset([1,2,3,4]) # nao deixa fazer update no SET
print(x)

a = set('Dieeeeeeego')
print(a)
print(4 not in a)

c1 = {1,2}
c2 = {2,3}
print(c1.union(c2))  # ira criar um terceira set nao alterando o c1
print("intersection " + str(c1.intersection(c2)))

print(c1.update(c2)) # ira adicionar os valores de c2 em c1 assim alterando ele

# verificar se c2 é um subconjunto de c1
print(c2 <= c1)

print({1,2,3} -{2}) # subtrair(diferença) entre dois conjuntos