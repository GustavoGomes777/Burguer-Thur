from bebida import Bebida

class Suco(Bebida):
    def __init__(self, sabor="Laranja", preco=5.00, tamanho="300ml"):
        super().__init__(f"Suco de {sabor}", preco, tamanho)
