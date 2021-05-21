# ira executar o else depois do for.
for x in range(1, 11):
    print(x)
else:
    print("--FIM---")

# nao ira executar o else se o break for encontrado.
for x in range(1, 11):
    if x == 10:
        break
    print(x)
else:
    print("---FIM---")
