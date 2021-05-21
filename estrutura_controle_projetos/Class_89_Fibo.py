#!/usr/local/bin/python3
# fibonacce -- sequencia de numeros somados ao seu antecessor.
# exemplo
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

# troca de variáveis


def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}')
    while ultimo <= limite:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci(int(input('Defina o valor do limite: ')))
