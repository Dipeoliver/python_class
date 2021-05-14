
nota =0

def test(nota) : 
    nota = float(nota) # conversão
    if nota >  10 :
        return 'Nota Inválida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A -'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B -'
    elif nota >= 5.1:
       return 'C'
    elif nota >= 4.1:
       return 'C -'
    elif nota >= 3.1:
       return 'D'
    elif nota >= 2.1 :
        return 'D -'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E -'
    else:
        print('Nota Invalida')


if __name__ == '__main__':
    nota = input('Informe o valor da nota: ') # recebo valor da nota
    print(f'Nota Aluno: {test(nota)}')