#include <stdio.h> //オムレツが大好きです。

int main() {

    //コメント
    printf(".-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-.");
    printf("| Bem vindo ao jogo de advinhação!!! |");
    printf("'-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-'");

    int numero_secreto = 42;

    int chute;

    printf("Chute um número inteiro: ");
    scanf("%d", &chute);
    printf("Seu chute foi %d\n", chute);

    if (chute == numero_secreto) {
        printf("Parabéns! Você acertou!");
    }

    else {
        if (chute > numero_secreto) {
            printf("Seu chute foi maior do que o número secreto!");
        }

        else {
            printf("Seu chute foi menor do que o número secreto!");
        }
    }

}