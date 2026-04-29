## mercado fds
import os

estoque = []; caixa = []; carrinho = []
def cadastrar_novo_produto():
    os.system('cls' if os.name == "nt" else 'clear')

    nome = input("Insira o nome do produto: ")
    quant = input("Insira a quantidade: ")
    valor = float(input("Insira o valor: "))
    estoque.append({"nome": nome, "quantidade": quant, "valor": valor})
    print("Produto cadastrado com sucesso! (^w^)")
    input("Pessione <ENTER> para continuar.")

def abastecer_estoque():
    os.system('cls' if os.name == "nt" else 'clear')

    nome = input("Insira o nome do produto a ser abastecido: ")

    for item in estoque:
        if item["nome"] == nome:
            quant = float(input("Digite a quantia de itens a serem abastecidos deste produto: "))
            item["quantidade"] += quant
            print("Produto abastecido com sucesso! :D\n")
            input("Pessione <ENTER> para continuar.")
            return
        
        print("Produto não encontrado! (Está escrito corretamente?) (-_x)")
        input("Pessione <ENTER> para continuar.")

def carrinho():
    os.system('cls' if os.name == "nt" else 'clear')

    print("Para encerrar a venda, digite 'VENDER'")
    print("Para retornar ao menu, digite 'RETORNAR'")
    nome = input("Insira o nome do produto a ser vendido: ")

    if nome.upper() == "RETORNAR":
        return
    
    elif nome.upper() == "VENDER":
        ##vender()
        return

    encontrado = False
    for item in estoque:
        if item["nome"] == nome:
            quant = float(input("Digite a quantia de itens a serem abastecidos deste produto: "))
            item["quantidade"] += quant
            print("Produto adicionado ao carrinho com sucesso! (*v*)\n")
            encontrado = True
            input("Pessione <ENTER> para continuar.")

    if encontrado == False:
        print("Produto não encontrado! (Está escrito corretamente?) (-_x)\n")
        input("Pessione <ENTER> para continuar.")

    carrinho()

def menu():
    while True:
        os.system('cls' if os.name == "nt" else 'clear')
        
        print(".=-=-=-=-=-=-=.")
        print("|   MERCADO   |")
        print("'=-=-=-=-=-=-='\n")

        print("Selecione uma opção: ")
        print("[1] - Cadastrar novo produto.")
        print("[2] - Abastecer estoque.")
        print("[3] - Editar carrinho.")
        print("[4] - Finalizar venda.")
        print("[5] - Ajuda.")
        print("[0] - sair do sistema.")

        opcao == input(": ")
        if opcao == "1":
            