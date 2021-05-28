#!/usr/local/bin/python3

arquivo = open('pessoas.csv')
# carrego todo o arquivo para memoria da maquina
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    # print(*registro.split(','))

    # ira separar o arquivo em duas partes atraves da virgula e pegar os argumentos variaveis
    print('Nome: {} | Idade: {}'.format(*registro.split(',')))
