from datetime import datetime

from loja import Cliente, Vendedor, Compra


def main():
    cliente = Cliente('Maria Lima', 44)
    vendedor = Vendedor('Diego Oliveira', 39, 6000)
    compra1 = Compra(cliente, datetime.noew(), 512)
    compra2 = Compra(cliente, datetime(2021, 7, 12), 256)

    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)

    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adult() else '')
    print(f'vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    qte_compras = len(cliente.compras)
    print(f'Total: {valor_total} em {qte_compras} compras')
    print(f'Ultima compra:{cliente.get_data_ultima_compra()}')

    if __name__ == '__init__':
        print('start')
        main()
