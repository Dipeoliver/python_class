
# fibonacce -- sequencia de numeros somados ao seu antecessor.
# exemplo
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}')
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo

        if proximo > 100000000000:
            break


if __name__ == '__main__':
    fibonacci()
