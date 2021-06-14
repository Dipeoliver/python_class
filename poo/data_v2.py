# construtor

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)
# d1.dia = 5
# d1.mes = 12
# d1.ano = 2019
print(d1)

# ------------------------------------------------------------------------
# posso adicionar parametros iniciais e nao passar nada na chamada


class Data2:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d2 = Data2()
d2.dia = 12
# d2.mes = 11
# d2.ano = 2020
print(d2)

d3 = Data2(ano=2022)
# d3.dia = 12
# d3.mes = 11
# d3.ano = 2020
print(d3)
