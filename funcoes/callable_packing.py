# funcao que calcula o preço final de um produto adicionando imposto.
# duas funcoes diferentes
                                                # packing
def calc_preco_final(preco_bruto, calc_imposto, *params):
                                                # unpacking
    return preco_bruto + preco_bruto * calc_imposto(*params)

def imposto_x(importado):
    return 0.22 if importado else 0.13

def imposto_y(explosivo, fator_multi=1):
    return 0.11 * fator_multi if explosivo else 0

if __name__ == "__main__":
    preco_bruto = 134.98
    preco_final = calc_preco_final(preco_bruto, imposto_x, True)
    print(preco_final)
    preco_final2 = calc_preco_final(preco_final, imposto_y,True,1.5)
    print(preco_final2)
    print("%.2f" % preco_final2)
    print(round(preco_final2,2))