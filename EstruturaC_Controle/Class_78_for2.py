palavra = 'paralalepipedo'
for letra in palavra:
    print(letra)  # aqui tem a quebra de linha \n

for letra in palavra:
    print(letra, end="")  # imprimir na mesma linha, tira a quebra de linha

print('Fim')

# imprimir lista
aprovados = ["Diego", "mario", "Jose", "Alfredo"]
for nome in aprovados:
    print(nome)

# imprimir lista com indice
for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)

# imprimir tupla
dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta')
for dia in dias_semana:
    print(f'Hoje é {dia}')

# imprimir um set
for letra in set('muito legal'):
    print(letra)
