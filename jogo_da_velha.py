def exibir_tabuleiro(tabuleiro):
    for i in range(3):
        print(f"{tabuleiro[i][0]} │ {tabuleiro[i][1]} │ {tabuleiro[i][2]}")
        if i < 2:
            print("━┿━┿━")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j]) == jogador for j in range(3):
            return True
        if all(tabuleiro[j][i]) == jogador for j in range(3):
            return True
        
    if tabuleiro[0][0] == jogador and tabuleiro [1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    
    
    