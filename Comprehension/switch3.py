def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana'
    }
    # tipo = descrição
    # numeros = tupla (identificação)
    #                    [expressão ,   for item in list ,   if condicional]
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** Data Inválida **')


if __name__ == "__main__":
    for dia in range(0, 9):
        print(f'{dia} : {get_tipo_dia(dia)}')
