class Potencia:
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente

if __name__ == '__main__':
    # expoente
    quadrado = Potencia(2)
    cubo = Potencia(3)


if  callable(quadrado) and callable(cubo):
                   # base
    print(f'3^2 = {quadrado(3)}')
    print(f'2^3 = {cubo(2)}')
             # expoente / base
    print(Potencia(3)(2))