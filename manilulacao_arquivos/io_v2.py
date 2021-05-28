#!/usr/local/bin/python3

arquivo = open('pessoas.csv')
# faz um streaming do arquivo
for registro in arquivo:
    print('Nome: {} | Idade: {}'.format(*registro.split(',')))
arquivo.close()
