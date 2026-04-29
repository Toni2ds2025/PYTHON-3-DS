## mercado fds
import os

estoque = []; caixa = []
def cadastrar_novo_produto():
    nome = input("Insira o nome do produto: ")
    quant = input("Insira a quantidade: ")
    valor = float(input("Insira o valor: "))
    estoque.append({"nome" : nome, "quantidade" : quant, "valor" : valor})
    print("Produto cadastrado com sucesso! (^w^)")

def abastecer_estoque():
    nome = input("Digite o nome do produto a ser abastecido: ")

    for item in estoque:
        if estoque