class Bebida:
    def __init__(self, nome, preco, tamanho):
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho  # Ex: 300ml, 500ml, 1L

    def __str__(self):
        return f"{self.nome} {self.tamanho} - R${self.preco:.2f}"
