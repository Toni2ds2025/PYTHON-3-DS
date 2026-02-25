#Calculadora Básica

import os
import platform

def cls():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

    inicio()

def inicio():
    print(".-------------------------.")
    print("|       CALCULADORA       |")
    print("'-------------------------'")

    print("\n\nDigite a Operação\n")
    print("[1] - Adição")
    print("[2] - Subtração")
    print("[3] - Multiplicação")
    print("[4] - Divisão")
    opcao = input(": ")

    if opcao == "1":
        print("\nAdição")
        n1 = float(input("\nDigite o Primeiro Valor: "))
        n2 = float(input("Digite o Segundo Valor: "))

        print("\nO Resultado é ", n1 + n2 ,".")
        input("\n\nPressione ENTER para prosseguir...")
        cls()

    elif opcao == "2":
        print("\nSubtração")
        n1 = float(input("\nDigite o Primeiro Valor: "))
        n2 = float(input("Digite o Segundo Valor: "))

        print("\nO Resultado é ", n1 - n2 ,".")
        input("\n\nPressione ENTER para prosseguir...")
        cls()

    elif opcao == "3":
        print("\nMultiplicação")
        n1 = float(input("\nDigite o Primeiro Valor: "))
        n2 = float(input("Digite o Segundo Valor: "))

        print("\nO Resultado é ", n1 * n2 ,".")
        input("\n\nPressione ENTER para prosseguir...")
        cls()

    elif opcao == "4":
        print("\nDivisão")
        n1 = float(input("\nDigite o Primeiro Valor: "))
        n2 = float(input("Digite o Segundo Valor: "))

        if n2 == 0:
            print("\nERRO: Divisão inválida!")
        else:
            print("\nO Resultado é ", n1 / n2 ,".")

        input("\n\nPressione ENTER para prosseguir...")
        cls()

    else:
        print("ERRO: Opção Inválida!")
        input("\n\nPressione ENTER para prosseguir...")
        cls()
cls()