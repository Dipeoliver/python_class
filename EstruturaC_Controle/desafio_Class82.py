
def get_dia_semana(dia):
    dias = {
        1: 'dia_Semana',
        2: 'dia_Semana',
        3: 'dia_Semana',
        4: 'dia_Semana',
        5: 'dia_Semana',
        6: 'Final_Semana',
        7: 'Final_Semana',
    }
    return dias.get(dia, 'Valor invalido')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')
