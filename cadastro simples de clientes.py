# .---------------------------------------------------.
# |  Sistema simples para cadastros de clientes       |
# |  Linguagem: Python                                |
# |  Objetivo: Demonstrar lógica básica de cadastro   |
# '---------------------------------------------------'

# Lista de que armazenará todos os clientes cadastrados
clientes = []

def cadastrar_cliente():
    """
    Função responsável por cadastrar um novo cliente
    """
    print("\n=== Cadastro de novo cliente ===")

    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    # Criando um dicionário com os dados do cliente

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "telefone": telefone
    }

    # Adicionando o cliente à lista de clientes
    clientes.append(cliente)

    print("\n Cliente cadastrado com sucesso!")

def listar_clientes():
    """
    Função responsável por listar todos os clientes cadastrados
    """
    print("\n=== Lista de Clientes ===")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    
    #Percorre a lista de clientes e exibe os dados
    for index, cliente in enumerate(clientes, start=1):
        print(f"\nCliente {index}")
        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"E-Mail: {cliente['email']}")
        print(f"Telefone: {cliente['telefone']}")

def buscar_cliente_por_cpf():
    """
    Função responsável por buscar um cliente pelo CPF
    """
    print("\n=== Buscar Cliente pelo CPF ===")
    cpf_procurado = input("Digite o CPF para busca: ")

    # Procura o cliente na lista
    for cliente in clientes:
        if cliente["cpf"] == cpf_procurado:
            print("\n Cliente encontrado: ")
            print(f"Nome: {cliente['nome']}")
            print(f"E-Mail: {cliente['email']}")
            print(f"Telefone: {cliente['Telefone']}")
            return
        
    print("\n Cliente não encontrado.")

def menu():
    """
    Exibe o menu principal do programa
    """
    print(".=-=-=-=-=-=-.")
    print("|    MENU    |")
    print("'-=-=-=-=-=-='\n")

    print("[1] - Cadastrar cliente")
    print("[2] - Listar clientes")
    print("[3] - Buscar clientes por CPF")
    print("[0] - Sair")

# --------------------
# Programa principal
# --------------------

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_cliente()
    elif opcao == '2':
        listar_clientes()
    elif opcao == '3':
        buscar_cliente_por_cpf()
    elif opcao == '0':
        print("\nEncerrando o sistema")
        break
    else:
        print("\nPor favor, insira uma opção válida!")