
nota =0

def test(nota) : 
    if nota >= 9.1 and nota <= 10 :
        print('Nota: A')
    elif nota >= 8.1 and nota <= 9 :
        print('Nota: A-')
    elif nota >= 7.1 and nota <= 8 :
        print('Nota: B')
    elif nota >= 6.1 and nota <= 7 :
        print('Nota: B-')
    elif nota >= 5.1 and nota <= 6 :
        print('Nota: C')
    elif nota >= 4.1 and nota <= 5 :
        print('Nota: C-')
    elif nota >= 3.1 and nota <= 4 :
        print('Nota: D')
    elif nota >= 2.1 and nota <= 3 :
        print('Nota: D-')
    elif nota >= 1.1 and nota <= 2 :
        print('Nota: E')
    elif nota >= 0 and nota <= 1 :
        print('Nota: E-')
    else:
        print('Nota Invalida')


if __name__ == '__main__':
    nota = input('Informe o valor da nota: ')
    test(float(nota))