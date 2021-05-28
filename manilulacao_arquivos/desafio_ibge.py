#!/usr/local/bin/python3
import csv
from urllib import request


def read():

    with open('desafio-ibge.csv') as entrada:
        dados = entrada.read()
        for registro in csv.reader(dados.splitlines()):
            print(f'{registro[8]}:  {registro[3]}')
            #     registro[4], registro[4]), )  # file=saida


if __name__ == "__main__":
    read()


# #!/usr/local/bin/python3
# import csv
# from urllib import request


# def read(url):

#     with request.urlopen(url) as entrada:
#         dados = entrada.read()
#         for registro in csv.reader(dados.splitlines()):
#             print(f'{registro[8]}:  {registro[3]}')
#             #     registro[4], registro[4]), )  # file=saida


# if __name__ == "__main__":
#     read(r"http://files.cod3r.com.br/curso-python/desafio-ibge.csv")
