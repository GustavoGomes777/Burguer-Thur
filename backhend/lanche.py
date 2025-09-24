from sanduiche import Lanche

class XSalada(Lanche):
    def __init__(self):
        super().__init__("X-Salada", 15.00, ["Pão", "Hambúrguer", "Queijo", "Alface", "Tomate"])

class XTudo(Lanche):
    def __init__(self):
        super().__init__("X-Tudo", 22.00, ["Pão", "Hambúrguer", "Queijo", "Presunto", "Bacon", "Ovo", "Alface", "Tomate"])
