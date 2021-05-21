from random import randint


def sortear_dado():
    return randint(1, 500)


for x in range(1, 501):
    if x % 2 == 1:
        continue
    if x == sortear_dado():
        print(f'Acertou o numero {x}')
        break
else:
    print(f'Nao e o numero {x}')

# if __name__ == '__main__':
    # print(sortear_dado())
