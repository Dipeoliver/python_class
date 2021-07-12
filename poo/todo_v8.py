# ***************     Tratamento de erro  *******************

from datetime import datetime, timedelta


class TarefaNaoecncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    # capaz de interar todas as tarefas dentro do projeto

    def __iter__(self):
        return self.tarefas.__iter__()

    # sobrecarga do operador +=
    # projeto += tarefa
    # casa += ...
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwergs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa1(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolha = self._add_tarefa if isinstance(tarefa, Tarefa1) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolha(tarefa, **kwargs)

    def pendentes(self):
        return [Tarefa1 for Tarefa1 in self.tarefas if not Tarefa1.feito]

    def procurar(self, descricao):
        try:
            # possivel indexERROR
            # se achar a descrição no laço tarefa ira retornar a 1° que achar
            return[Tarefa1 for Tarefa1 in self.tarefas if Tarefa1.descricao == descricao][0]
        except IndexError as e:
            raise TarefaNaoecncontrada(str(e))

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


# abaixo exemplo de herança
class TarefaRecorrente(Tarefa1):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento=vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():

    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Fazer comida', datetime.now() + timedelta(days=3))
    casa.add('Lavar prato')
    casa += TarefaRecorrente('Trocar lencois', datetime.now(), 7)
    casa.procurar('Trocar lencois').concluir()

    try:
        # forçar a dar um erro
        casa.procurar('Trocar lencois - erro')
    except TarefaNaoecncontrada as e:
        print(f'A causa foi {str(e)}')
    finally:
        print('sempre sera executado')

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
