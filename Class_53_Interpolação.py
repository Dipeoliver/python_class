nome, idade = 'Diego', 30.9874

# %s string
# %d decimal (parte inteira)
# %f float   (valor com casas decimais)
# .2 duas casas decimais
# %r valores Bool
# %s valores Bool
print('nome: %s idade: %.2f %r %s' % (nome,idade, True, False)) # versão mais antiga, não se usa muito

print({'Nome:{0}'})