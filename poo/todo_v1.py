from datetime import datetime


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
    casa = []
    casa.append(Tarefa1('Passar roupa'))
    casa.append(Tarefa1('Lavar prato'))

    [Tarefa1.concluir() for Tarefa1 in casa if Tarefa1.descricao == 'Lavar prato']

    for Tarefa in casa:
        print(f'- {Tarefa}')


if __name__ == '__main__':
    main()
