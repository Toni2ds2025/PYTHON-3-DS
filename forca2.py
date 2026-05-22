import random

palavras = ["honami","saki","mafuyu","toya","ichika"]

def escolher_palavra():
    return random.choice(palavras)

def jogo():
    palavra = escolher_palavra()
    letras_descobertas = ["_"]
    tentativas = 6
    letras_usadas = []

    print("Bem vindo ao jogo da Forca!")

    while tentativas > 0 and "-" in letras_descobertas:
        print("\nPalavra: ", " ".join(letras_descobertas))
        print("Letras usadas:", " ".join(letras_usadas))
        print("Tentativas restantes: ", tentativas)

        letra = input("Digite uma letra: ").lower()

        if letra in letras_usadas:
            print("Você já tentou essa letra!")
            continue

        letras_usadas.append(letra)

        if letra in palavra:
            print("Letra correta, ")
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_descobertas[i] = letra
        else:
            print("Letra errada!.")
            tentativas -= 1
    if "_" not in letras_descobertas:
        print("\nParabéns! Você venceu! A palavra era: ", palavra)
    else:
        print("\nVocê perdeu! A palavra era: ", palavra)

if __name__ == "__main__":
    jogo()