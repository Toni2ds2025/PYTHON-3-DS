## mercado fds
import os

estoque = []; caixa = []; carrinho = []
def cadastrar_novo_produto():
    nome = input("Insira o nome do produto: ")
    quant = input("Insira a quantidade: ")
    valor = float(input("Insira o valor: "))
    estoque.append({"nome": nome, "quantidade": quant, "valor": valor})
    print("Produto cadastrado com sucesso! (^w^)")

def abastecer_estoque():
    nome = input("Insira o nome do produto a ser abastecido: ")

    for item in estoque:
        if item["nome"] == nome:
            quant = input("Digite a quantia de itens a serem abastecidos deste produto: ")
            item["quantidade"] += quant
            print("Produto abastecido com sucesso! :D\n")
            return
        
        print("Produto não encontrado! (Está escrito corretamente?) (-_x)")

def vender():
    nome = input("Insira o nome do produto: ")
    quant = float(input("Insira a quantia a ser vendida: "))
    carrinho.append("nome": nome, "quantidade": quant)