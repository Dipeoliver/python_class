# [expressão for item in list if condicional]
dobros = [i*2 for i in range(10) if i % 2 == 0]
print(dobros)


# versão normal
dobros = []
for i in range(10):
    if i % 2 == 0:
        dobros.append(i*2)
print(dobros)
