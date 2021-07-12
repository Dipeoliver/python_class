from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    # capaz de interar todas as tarefas dentro do projeto

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa1(descricao, vencimento))

    def pendentes(self):
        return [Tarefa1 for Tarefa1 in self.tarefas if not Tarefa1.feito]

    def procurar(self, descricao):
        # possivel indexERROR

        # se achar a descrição no laço tarefa ira retornar a 1° que achar
        return[Tarefa1 for Tarefa1 in self.tarefas if Tarefa1.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa1:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        # popular o status
        if self.feito:
            status.append('(concluida)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencido)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(vence em {dias} dias)')

        return f'{self.descricao}' + ' '.join(status)


def main():

    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Fazer comida', datetime.now() + timedelta(days=3))
    casa.add('Lavar prato')
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for Tarefa1 in casa:
        print(f'-{Tarefa1}')
    print(casa)

    # print('///////////////////////////////////')

    # mercado = Projeto('Compras no mercado')
    # mercado.add('Frutas secas')
    # mercado.add('Carne')
    # mercado.add('Tomate')
    # print(mercado)
    # mercado.procurar('Frutas secas').concluir()
    # for Tarefas1 in mercado:
    #     print(f'-{Tarefas1}')


if __name__ == '__main__':
    main()
