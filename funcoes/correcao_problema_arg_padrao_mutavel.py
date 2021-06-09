def fibonaci(sequencia=None):
    # se o primeiro item for falso retorna o segundo
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonaci()
    print(inicio, id(inicio))
    print(fibonaci(inicio))
    restart = fibonaci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
