class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def descrever_produto(self):
        return f"{self.nome}: R${self.preco:.2f}, {self.quantidade} unidades em estoque."
        
    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade
            print(f"{quantidade} unidades adicionadas ao estoque.")
        else:
            print("Quantidade inválida para adicionar ao estoque.")

    def vender_produto(self, quantidade):
        if 0 < quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f"{quantidade} unidades vendidas.")
        else:
            print("Quantidade inválida ou estoque insuficiente.")

# Criando uma instância da classe Produto:
meu_produto = Produto("Notebook", 2500.00, 10)

# Usando os métodos da classe:
print(meu_produto.descrever_produto())  # Saída: Notebook: R$2500.00, 10 unidades em estoque.
meu_produto.adicionar_estoque(5)        # Saída: 5 unidades adicionadas ao estoque.
print(meu_produto.descrever_produto())  # Saída: Notebook: R$2500.00, 15 unidades em estoque.
meu_produto.vender_produto(3)           # Saída: 3 unidades vendidas.

print(meu_produto.descrever_produto())  # Saída: Notebook: R$2500.00, 12 unidades em estoque.
