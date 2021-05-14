nome = 'Diego Oliveira'
idade = 39
altura = round(1.71,2)
peso = 74.5
anoAtual = 2021
anodeNascimento = anoAtual - idade
imc = round(peso /( altura**2),2)

resultado = f'''O senhor {nome} com idade de {idade} anos, 
altura {altura:3} metros e peso de {peso} Kg 
nasceu em {anodeNascimento} e tem o IMC de {imc} '''

print(resultado)