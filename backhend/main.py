from sanduiche import Lanche
from lanche import XSalada, XTudo
from refrigerante import Refrigerante
from suco import Suco
from agua import Agua
from cardapio import Cardapio

def menu():
    print("\n🍔 THUR Burger - Sistema de Cardápio")
    print("1. Adicionar Sanduíche")
    print("2. Adicionar Bebida")
    print("3. Adicionar Lanche Padrão (X-Salada ou X-Tudo)")
    print("4. Mostrar Cardápio")
    print("5. Sair")

def main():
    cardapio = Cardapio()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do sanduíche: ")
            preco = float(input("Preço: "))
            ingredientes = []
            qtd = int(input("Quantos ingredientes? "))
            for i in range(qtd):
                ingredientes.append(input(f"Ingrediente {i+1}: "))
            lanche = Lanche(nome, preco, ingredientes)
            cardapio.adicionar_item(lanche)

        elif opcao == "2":
            print("\n--- Escolha a bebida ---")
            print("1. Refrigerante")
            print("2. Suco")
            print("3. Água")
            escolha = input("Digite a opção: ")

            if escolha == "1":
                nome = input("Nome do refrigerante: ")
                preco = float(input("Preço: "))
                tamanho = input("Tamanho (ex: 350ml): ")
                refri = Refrigerante(nome, preco, tamanho)
                cardapio.adicionar_item(refri)

            elif escolha == "2":
                sabor = input("Sabor do suco: ")
                preco = float(input("Preço: "))
                tamanho = input("Tamanho (ex: 300ml): ")
                suco = Suco(sabor, preco, tamanho)
                cardapio.adicionar_item(suco)

            elif escolha == "3":
                tipo = input("Tipo da água (ex: Mineral, Com Gás): ")
                preco = float(input("Preço: "))
                tamanho = input("Tamanho (ex: 500ml): ")
                agua = Agua(tipo, preco, tamanho)
                cardapio.adicionar_item(agua)

            else:
                print("Opção inválida!")

        elif opcao == "3":
            escolha = input("Digite [1] para X-Salada ou [2] para X-Tudo: ")
            if escolha == "1":
                cardapio.adicionar_item(XSalada())
            elif escolha == "2":
                cardapio.adicionar_item(XTudo())
            else:
                print("Opção inválida!")

        elif opcao == "4":
            cardapio.mostrar_cardapio()

        elif opcao == "5":
            print("Saindo... Obrigado por usar o sistema! 🍔")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()


