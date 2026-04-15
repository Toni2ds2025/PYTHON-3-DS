##UwU

clientes = []; fornecedores = []; estoque = []; vendas = []; contas_pagar = []; contas_receber = []

def cadastrar_cliente():
    nome = input("Nome do Cliente: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    clientes.append({"nome": nome, "cpf": cpf, "telefone": telefone})
    print("CLiente cadastrado com sucesso (^w^)\n")

def cadastrar_fornecedor():
    nome = input("Nome do Fornecedor: ")
    cnpj = input("CNPJ: ")
    produto = input("Produto fornecido: ")
    fornecedores.append({"nome": nome, "cnpj": cnpj, "produto": produto})
    print("Fornecedor cadastrado com sucesso! (^w^)\n")

def cadastrar_produto():
    nome = input("Nome do produto: ")
    quant = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    estoque.append({"nome": nome, "quant": quant, "preco": preco})
    print("Produto cadastrado com sucesso! (^w^)\n")

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
            print(f"Venda registrada! Total: R${total:.2f}. (^w^)\n")
            return
        print("Produto não encontrado ou estoque insuficiente! (-_=)\n")

def registrar_conta_pagar():
    fornecedor = input("Nome do fornecedor: ")
    valor = float(input("Valor: "))
    data = input("Data de vencimento: ")
    contas_pagar.append({"fornecedor": fornecedor, "valor": valor, "data": data})
    print("Conta a pagar registrada com sucesso! (^w^)\n")

def exibir_relatorios():
    print("\n> Clientes (~_~)")
    for c in clientes:
        print(c)

    print("\n> Fornecedores (>~<)")
    for f in fornecedores:
        print(f)

    print("\n> Estoque (*-*)")
    for e in estoque:
        print(e)

    print("\n> Vendas (^U^)")
    for v in vendas:
        print(v)

    print("\n> Contas a pagar (O_O)")
    for cp in contas_pagar:
        print(cp)

    print("\n> Contas a receber ($w$)")
    for cr in contas_receber:
        print(cr)

def menu():
    while True:
        print("\n.=-=-=-=-=-=-=-=-=-=.")
        print("| Sistema de Gestão |")
        print("'=-=-=-=-=-=-=-=-=-='")

        print("[1] - Cadastrar Cliente.")
        print("[2] - Cadastrar Fornecedor.")
        print("[3] - Cadastrar Produto no Estoque.")
        print("[4] - Registrar Venda.")
        print("[5] - Registrar Contas a Pagar.")
        print("[6] - Exibir Relatórios.")
        print("[0] - Sair.")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente()

        elif opcao == '2':
            cadastrar_fornecedor()

        elif opcao == '3':
            cadastrar_produto()

        elif opcao == '4':
            registrar_venda()
        
        elif opcao == '5':
            registrar_conta_pagar()

        elif opcao == '6':
            exibir_relatorios()

        elif opcao == '0':
            print("Saindo do Sistema... (T_T)")
            break

        else:
            print("Opção inválida! (+_x)")

menu()