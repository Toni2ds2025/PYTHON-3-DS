##UwU

clientes = []; fornecedores = []; estoque = []; vendas = []; contas_pagar = []; contas_receber = []

def cadastrar_cliente():
    nome = input("Nome do Cliente: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    clientes.append({"nome": nome, "cpf": cpf, "telefone": telefone})
    print("CLiente cadastrado com sucesso!\n")
def cadastrar_fornecedor():
    nome = input("Nome do Fornecedor: ")
    cnpj = input("CNPJ: ")
    produto = input("Produto fornecido: ")
    fornecedores.append({"nome": nome, "cnpj": cnpj, "produto": produto})
    print("Fornecedor cadastrado com sucesso!\n")

def cadastrar_produto():
    nome = input("Nome do produto: ")
    quant = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    estoque.append({"nome": nome, "quant": quant, "preco": preco})
    print("Produto cadastrado com sucesso!\n")

def registrar_venda():
    cliente = input("Nome do cliente: ")
    produto = input("Produto vendido: ")
    quant = int(input("Quantidade: "))
    for item in estoque:
        if item["nome"] == produto and item["quantidade"] >= quant:
            item["quant"] -= quant
            total = quant * item[preco]
            vendas.append({"cliente": cliente, "produto": produto, "quant": quant, "total": total})
            contas_receber.append({"cliente": cliente, "valor": total})
            print(f"Venda registrada! Total: R${total:.2f}\n")
            return
        print("Produto não encontrado ou estoque insuficiente!\n")
