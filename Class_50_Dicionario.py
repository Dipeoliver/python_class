pessoas = {'nome': 'Diego','idade': 39, 'cursos': ['ingles','portugues']}
print(type(pessoas))

print(pessoas)
print(len(pessoas))

print(pessoas['nome'])
print(pessoas['idade']) # pegar valores
print(pessoas['cursos'])
print(pessoas['cursos'][1]) # acessando a lisat de indice um
print(pessoas.keys())
print(pessoas.values()) # pegar valores
print(pessoas.items())

print(pessoas.get('idade')) # pegar valores
print(pessoas.get('tag',['123'])) # se nao tiver dentro do dicionario passa valor default
