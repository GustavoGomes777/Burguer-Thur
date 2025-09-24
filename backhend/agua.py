from bebida import Bebida

class Agua(Bebida):
    def __init__(self, tipo="Mineral", preco=3.00, tamanho="500ml"):
        super().__init__(f"Água {tipo}", preco, tamanho)
