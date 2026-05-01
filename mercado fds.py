## mercado
import os

estoque = []; caixa = []; carrinho = []
def cadastrar_novo_produto():
    os.system('cls' if os.name == "nt" else 'clear')

    nome = input("Insira o nome do produto: ").upper()
    if nome == "":
        print("Insira um valor! (x_X)")
        input("Pressione <ENTER> para continuar.")
        cadastrar_novo_produto()

    elif nome == "CANCELAR" or nome == "RETORNAR" or nome == "REMOVER":
        print("Insira um valor válido! (u.u)")
        input("Pessione <ENTER> para continuar.")
        cadastrar_novo_produto()
    
    print("Insira a forma de medida: ")
    print("[KG] - Quilograma")
    print("[UN] - Unidade")
    print("[L] - Litros")
    medida = input(": ").upper()

    if medida == "":
        print("Insira um valor! (x_X)")
        input("Pressione <ENTER> para continuar.")
        cadastrar_novo_produto()

    elif medida != "KG" or medida != "UN" or medida != "L":
        print("Insira um valor válido! (u.u)")
        input("Pessione <ENTER> para continuar.")
        cadastrar_novo_produto()

    valor = float(input("Insira o valor: "))
    if valor == "":
        print("Insira um valor! (x_X)")
        input("Pressione <ENTER> para continuar.")
        cadastrar_novo_produto()
    valor = float(valor)

    estoque.append({"nome": nome, "medida": medida, "valor": valor})
    print("Produto cadastrado com sucesso! (^w^)")
    input("Pessione <ENTER> para continuar.")

def abastecer_estoque():
    os.system('cls' if os.name == "nt" else 'clear')

    print("Digite [CANCELAR] para cancelar o abastecimento")
    nome = input("Insira o nome do produto a ser abastecido: ").upper()

    if nome == "CANCELAR":
        menu()

    for item in estoque:
        if item["nome"] == nome:
            quant = float(input("Digite a quantia de itens a serem abastecidos deste produto: "))
            item["quantidade"] += quant
            print("Produto abastecido com sucesso! :D\n")
            input("Pessione <ENTER> para continuar.")
            return
        
        print("Produto não encontrado! (Está escrito corretamente?) (-_x)")
        input("Pessione <ENTER> para continuar.")

def editar_carrinho():
    os.system('cls' if os.name == "nt" else 'clear')

    print(".=-=-=-=-==-=-=.")
    print("| Carrinho ⪿ⵗ´ |")
    print("'=-=-=-=-==-=-='\n")

    print("Para adicionar um item ao carrinho, apenas insira o seu nome\n")

    print("Outros comandos:")
    print("[VENDER] - Encerrar a venda")
    print("[RETORNAR] - Retornar ao menu")
    print("[REMOVER] - Remover um item do carrinho")
    nome = input("Insira o nome do produto a ser vendido: ").upper()

    if nome == "RETORNAR":
        return
    
    elif nome == "VENDER":
        ##vender()
        return
    
    elif nome == "REMOVER":
        print("\nPara remover um item do carrinho, apenas insira o seu nome\n")
        print("Outros comandos:")
        print("[CANCELAR] - cancela a remoção")
        nome = input("\nInsira o nome do produto a ser removido: ").upper()
        
        if nome == "CANCELAR":
            editar_carrinho()
        
        encontrado = False
        for i in range(len(carrinho) - 1, -1, -1):
            if carrinho[i]["nome"] == nome:
                carrinho.pop(i)
                print("Item removido com sucesso! (^u^)")
                encontrado = True

        if encontrado == False:
            print("Produto não encontrado! (Está escrito corretamente?) (-_x)\n")
            input("Pessione <ENTER> para continuar.")
        
        editar_carrinho()

    encontrado = False
    for item in estoque:
        if item["nome"] == nome:
            quant = float(input("Digite a quantia de itens a serem adicionados deste produto: "))
            item["quantidade"] += quant
            print("Produto adicionado ao carrinho com sucesso! (*v*)\n")
            encontrado = True
            input("Pessione <ENTER> para continuar.")

    if encontrado == False:
        print("Produto não encontrado! (Está escrito corretamente?) (-_x)\n")
        input("Pessione <ENTER> para continuar.")

    editar_carrinho()

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

        opcao = input(": ")
        if opcao == "1":
            cadastrar_novo_produto()
        
        elif opcao == "2":
            abastecer_estoque()

        elif opcao == "3":
            editar_carrinho()
        
        elif opcao == "4":
            ##vender()
            menu()
        
        elif opcao == "5":
            ##ajuda()
            menu()
        elif opcao == "0":
            os.system('cls' if os.name == "nt" else 'clear')
            print("Programa encerrado! (OwO)")
            break

        else:
            print("Insira uma opção válida!! (=_-)")

menu()
            