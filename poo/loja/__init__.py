# pessoa nao preciso expor fora do pacote

from .cliente import Cliente
from .vendedor import Vendedor
from .compra import Compra

__all__ = ['Cliente', 'Vendedor', 'Compra']
