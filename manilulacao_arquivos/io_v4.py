#!/usr/local/bin/python3

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {} | Idade: {}'.format(*registro.strip().split(',')))
except:
    print('erro')

finally:
    arquivo.close()
