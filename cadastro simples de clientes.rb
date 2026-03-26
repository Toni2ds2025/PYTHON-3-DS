# .---------------------------------------------------.
# |  Sistema simples para cadastros de clientes       |
# |  Linguagem: Python                                |
# |  Objetivo: Demonstrar lógica básica de cadastro   |
# '---------------------------------------------------'

# Lista de que armazenará todos os clientes cadastrados
clientes= []

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
        "email": email
        "telefone": telefone
    }

    # Adicionando o cliente à lista de clientes
    clientes.append(cliente)