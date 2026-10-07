#Jogo da velha

from random import randrange
tm = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

while True:
    for i in range(10):
        print(randrange(8))

    print("+---+---+---+")
    print(f"| {tm[0][0]} | {tm[0][1]} | {tm[0][2]} |")
    print("+---+---+---+")
    print(f"| {tm[1][0]} | {tm[1][1]} | {tm[1][2]} |")
    print("+---+---+---+")
    print(f"| {tm[2][0]} | {tm[2][1]} | {tm[2][2]} |")
    print("+---+---+---+")

    if tm[0][0] == tm[0][1] == tm[0][2]:
        if [0][0] == "O":
            print("Você venceu")
            break
        else:
            print("Você perdeu!")
            break

    elif tm[1][0] == tm[1][1] == tm[1][2]:
        if [1][0] == "O":
            print("Você venceu")
            break
        else:
            print("Você perdeu!")
            break

    elif tm[2][0] == tm[2][1] == tm[2][2]:
        if [2][0] == "O":
            print("Você venceu")
            break
        else:
            print("Você perdeu!")
            break

    elif tm[0][0] == tm[1][1] == tm[2][2]:
        if [0][0] == "O":
            print("Você venceu")
            break
        else:
            print("Você perdeu!")
            break

    elif tm[2][0] == tm[1][1] == tm[0][2]:
        if [2][0] == "O":
            print("Você venceu")
            break
        else:
            print("Você perdeu!")
            break

    elif tm[0][0] != "1" and tm[0][1] != "2" and tm[0][2] != "3" and tm[1][0] != "4" and tm[1][1] != "5" and tm[1][2] != "6" and tm[2][0] != "7" and tm[2][1] != "8" and tm[2][2] != "9":
        print("O jogo empatou!")
        break

    else:
        escolha = input("Escolha uma posição: ")
        break