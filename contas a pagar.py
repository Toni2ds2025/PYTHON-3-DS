#importando a bibliotexa pandas para a manipulação de dados
import pandas as pd

#Inicializando uma lista vazia para armazenar os clientes e contas a receber
clientes = []
contas_a_receber = []

#Função para adicionar um cliente
def add_cliente(codego, nome, telemoveloutelefixo, email):
    cliente = {
        'Codeigo': codego,
        'Nome': nome,
        'Telefone': telemoveloutelefixo,
        'Email': email
    }
    clientes.append(cliente)

#Função para adicionar uma conta a receber
def add_conta_a_receber(codego_cliente, descricao, valor, data_vencimento):
    conta = {
        'Código cliente': codego_cliente,
        'Descrição': descricao,
        'Valor': valor,
        'Data de vencimento': data_vencimento
    }
    contas_a_receber.append(conta)

#Função para exibir todos os clientes cadastrados
def exibir_clientes():
    df = pd.DataFrame(clientes)
    print(df)

def exibir_contas_a_receber():
    df = pd.DataFrame(contas_a_receber)
    print(df)

#Adicionando alguns clientes de exemplo
add_cliente(1, 'Ana Silva', '1234-5678', 'ana@exemplo.com')
add_cliente(1, 'João Souza', '9876-5432', 'joao@exemplo.com')

#Adicionando algumas contas a receber
add_conta_a_receber(1, 'Serviços de consultoria', 1500.00, '2025-05-10')
add_conta_a_receber(2, 'Venda de produtos', 300.00, '2025-05-15')

#exibindo clientes cadastrados
print("Clientes cadastrados")
exibir_clientes()

#Exibindo as contas a receber
print("\nContas a receber")
exibir_contas_a_receber()