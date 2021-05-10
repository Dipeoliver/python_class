# tupla nao aceita mudar os valores
# tupla e uma estrutura indexada

print(dir(tuple)) # verificar o que contem dentro da tupla

tupla = ('um',)
print(type(tupla))
print(tupla)

print(tupla[0])

cores=('verde','amarelo','azul')
print(cores[-1])

print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))