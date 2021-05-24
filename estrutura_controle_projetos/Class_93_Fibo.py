#!/usr/local/bin/python3
# fibonacce -- sequencia de numeros somados ao seu antecessor.
# exemplo
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

# vou determinar a quantidade de repetições que quero
def fibonacci(quantidade):
    resultado = [0, 1]
    for i in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    # listar os 20 primeiros números da sequência.
    for fib in fibonacci(int(input('Defina a quantidade de repetições do loop: '))):
        print(fib)
