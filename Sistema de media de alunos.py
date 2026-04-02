# UwU

alunos = []

def cadastrar_aluno():

    print("\n.=-=-=-=-=-=-=-=-=-=.'")
    print("| CADASTRO DE ALUNO |")
    print("'=-=-=-=-=-=-=-=-=-='\n")

    nome = input("Informe o Nome do Aluno: ")
    nota1 = float(input("Digite a 1ª Nota: "))
    nota2 = float(input("Digite a 2ª Nota: "))
    
    media = (nota1 + nota2) / 2
    
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
        
    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "situacao": situacao,
    }
    
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")
    
    
def listar_aluno():
    print("\n.=-=-=-=-=-=-=-=-=.")
    print("| LISTA DE ALUNOS |")
    print("'=-=-=-=-=-=-=-=-='\n")

    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Nota 1: {aluno['nota1']:.2f}")
        print(f"Nota 2: {aluno['nota2']:.2f}")
        print(f"Media 2: {aluno['media']:.2f}")
        print(f"Situação: {aluno['situacao']}")
        print("-" * 30)
        
def menu():
    while True:
        print("\n.=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.")
        print("| SISTEMA DE LANÇAMENTO DE NOTAS |")
        print("'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='\n")

        print("[1] - Cadastrar Aluno")
        print("[2] - Listar Alunos")
        print("[3] - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()

        elif opcao == '2':
            listar_aluno()

        elif opcao == '3':
            print("Sistema Encerrado.")
            break

        else:
            print("Insira uma Opção Válida!")

menu()