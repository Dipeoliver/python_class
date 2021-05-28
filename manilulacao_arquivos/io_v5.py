#!/usr/local/bin/python3

# 'with' abre e fecha o arquivo automatico
with open('pessoas.csv') as arquivo:

    for registro in arquivo:
        print('Nome: {} | Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('arquivo fechou')
