class Cardapio:
    def __init__(self):
        self.itens = []
        self._carregar_itens_padrao()  # já carrega os padrões

    def adicionar_item(self, item):
        self.itens.append(item)

    def mostrar_cardapio(self):
        print("\n=== CARDÁPIO ===")
        for i, item in enumerate(self.itens, 1):
            print(f"{i}. {item}")
        print("================\n")

    def _carregar_itens_padrao(self):
        """Adiciona os lanches e bebidas fixos no cardápio inicial"""
        from lanche import XSalada, XTudo
        from refrigerante import Refrigerante
        from suco import Suco
        from agua import Agua

        # Lanches fixos
        self.itens.append(XSalada())
        self.itens.append(XTudo())

        # Bebidas fixas
        self.itens.append(Refrigerante("Coca-Cola", 6.00, "350ml"))
        self.itens.append(Refrigerante("Guaraná", 5.50, "350ml"))
        self.itens.append(Suco("Laranja", 5.00, "300ml"))
        self.itens.append(Suco("Uva", 5.50, "300ml"))
        self.itens.append(Agua("Mineral", 3.00, "500ml"))
        self.itens.append(Agua("Com Gás", 4.00, "500ml"))
