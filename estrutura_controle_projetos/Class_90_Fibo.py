#!/usr/local/bin/python3
# fibonacce -- sequencia de numeros somados ao seu antecessor.
# exemplo
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

# troca de variáveis


def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(int(input('Defina o valor do limite: '))):
        print(fib)
