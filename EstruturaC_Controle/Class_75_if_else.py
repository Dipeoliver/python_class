def faixa_etaria(idade):

    idade = float(idade)
    if 0 <= idade < 18:           # tipo de intervalo
        return 'Menor de Idade'
    elif idade in range(18,65):   # tipo de intervalo por range (65 por so vai ate 64)
        return 'Adulto'
    elif idade in range(65,100):
        return 'Idoso'
    elif idade>= 100:
        return 'Centenáro' 
    else:
        return 'Idade invalida'

if __name__ == '__main__':

    # *****entrada de dados manual *****

    # idade = input('Qual a sua idade?')
    # if idade .isnumeric():
    #     print('Você é:', faixa_etaria(idade))
    # else:
    #     print("Idade tem de ser valor numérico")

    for idade in (17,35 ,87, 113,-2):
        print(f'{idade}: {faixa_etaria(idade)}')