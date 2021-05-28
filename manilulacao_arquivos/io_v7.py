#!/usr/local/bin/python3
import csv
# nao precisa colocar .split() ou .strip() a biblioteca ja faz isso
with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {} | Idade: {}'.format(*pessoa))
