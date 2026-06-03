import random
import subprocess
import os

def limpar_tela():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def criar_tabuleiro():
    return[['~' for _ in range(5)] for _ in range(5)]

def exibir_tabuleiro():
    print("\n   0   1   2   3   4")
    print("  " + "---+" * 4 + "---")
    for i, linha in enumerate(tabuleiro):
        print(f"{i} | " + " | ".join(linha) + " | ")
        if i < 4:
            print("  " + "---+" * 4 + "---")
    print("\n")