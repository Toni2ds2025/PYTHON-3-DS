def exibir_tabuleiro(tabuleiro):
    for i in range(3):
        print(f"{tabuleiro[i][0]} │ {tabuleiro[i][1]} │ {tabuleiro[i][2]}")
        if i < 2:
            print("━┿━┿━")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
        if all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
        
    if tabuleiro[0][0] == jogador and tabuleiro [1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    
    return False

def jogo_da_velha():
    tabuleiro = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    posicoes = {
        "1": (0, 0),
        "2": (0, 1),
        "3": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "7": (2, 0),
        "8": (2, 1),
        "9": (2, 2),
    }

    jogador_atual = "X"
    jogadas = 0

    print("┏━━━━━━━━━━━━━━━┓\n┃ JOGO DA VELHA ┃\n┗━━━━━━━━━━━━━━━┛\n")
    print("Para jogar, escolha o número correspondente à posição desejada.")

    while jogadas < 9:
        exibir_tabuleiro(tabuleiro)
        escolha = input(f"Jogador [{jogador_atual}], escolha uma posição (1-9): ").strip()
        if escolha not in posicoes:
            print("Opção inválida! Escolha um número de 1 a 9!")

        linha, coluna = posicoes[escolha]

        if tabuleiro[linha][coluna] in ["X", "O"]:
            print("Esta posição já está ocupada! Tente outra!")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1