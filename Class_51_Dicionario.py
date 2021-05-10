pessoas = {'nome': 'Diego','idade': 39, 'cursos': ['ingles','portugues']}

pessoas['idade'] = 30 # alterar o valor do dicionario
print(pessoas)

pessoas['cursos'].append('Angular') # adicionar item no Dicionário
print(pessoas)

pessoas.pop('idade')  # deapaga valores do dicionario
print(pessoas)

pessoas.update({'idade' : 40,'sexo':'M'}) # update de itens no dicionario
print(pessoas)

# não consegui deletar um item dentro da lista no dicionario
pessoas['cursos'].remove('portugues')
print(pessoas)


pessoas.clear()
print(pessoas)
