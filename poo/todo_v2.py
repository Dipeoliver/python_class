from datetime import datetime
from typing import Sequence


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa1(descricao))

    def pendentes(self):
        return [Tarefa1 for Tarefa1 in self.tarefas if not Tarefa1.feito]

    def procurar(self, descricao):
        # possivel indexERROR

        # se achar a descrição no laço tarefa ira retornar a 1° que achar
        return[Tarefa1 for Tarefa1 in self.tarefas if Tarefa1.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa1:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (concluida)' if self.feito else '')


def main():

    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for Tarefa1 in casa.tarefas:
        print(f'-{Tarefa1}')
    print(casa)

    print('///////////////////////////////////')

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate')
    print(mercado)
    mercado.procurar('Frutas secas').concluir()
    for Tarefas1 in mercado.tarefas:
        print(f'-{Tarefas1}')


if __name__ == '__main__':
    main()
