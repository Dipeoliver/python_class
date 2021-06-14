
class Carro():
    def __init__(self, velocidade_Maxima):
        self.velocidade_Maxima = velocidade_Maxima
        self.velocidade_Atual = 0

    def acelerar(self, delta=5):
        maxima = self.velocidade_Maxima
        nova = self.velocidade_Atual + delta
        self.velocidade_Atual = nova if nova <= maxima else maxima
        return self.velocidade_Atual

    def frear(self, delta=5):
        nova = self.velocidade_Atual - delta
        self.velocidade_Atual = nova if nova >= 0 else 0
        return self.velocidade_Atual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))
