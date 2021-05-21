
# continue - continua no laço for
# irá imiprimir apenas numeros impares
for x in range(1, 11):
    if x % 2 == 0:  # (%2) numeros divisiveis por 2
        continue    # pula a sequencia
    print(x)

print("----------")


# break - sai do laço for
for x in range(1, 11):
    if x == 5:  # quando x for 5 entra no break
        break
    print(x)
