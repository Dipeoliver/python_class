#!/usr/local/bin/python3

# .strip() para tirar espaços na laterais de strigs
# .strip(00) irá tirar zeros da string


arquivo = open('pessoas.csv')
# faz um streaming do arquivo
for registro in arquivo:
    print('Nome: {} | Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()
