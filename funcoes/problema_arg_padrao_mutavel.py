def fibonaci(sequencia=[0, 1]):
    # Uso de mutáveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonaci()
    print(inicio, id(inicio))
    print(fibonaci(inicio))
    restart = fibonaci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
