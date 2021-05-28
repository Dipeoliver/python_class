#!/usr/local/bin/python3

# 'with' abre e fecha o arquivo automatico
with open('pessoas.csv') as arquivo:
    # escrever em um arquivo 'gravar'
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            # estou fazendo print dentro de um arquivo 'salvando'
            print('Nome: {} | Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('arquivo fechou')
