from bebida import Bebida

class Refrigerante(Bebida):
    def __init__(self, nome="Coca-Cola", preco=6.00, tamanho="350ml"):
        super().__init__(nome, preco, tamanho)
