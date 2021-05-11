from string import Template

nome  = 'Diego'
idade = 30

# %s string
# %d decimal (parte inteira)
# %f float   (valor com casas decimais)
# .2 duas casas decimais
# %r valores Bool
# %s valores Bool
print('nome: %s idade: %.2f %r %s' % (nome,idade, True, False)) # versão mais antiga, não se usa muito

print('Nome:{0} Idade:{1}'.format(nome, idade)) # python < 3.6

print(f'Nome: {nome} Idade:{idade}') # python > 3.6

s = Template('Nome: $n ' 'Idade: $i')
print(s.substitute(n=nome, i=idade)) 