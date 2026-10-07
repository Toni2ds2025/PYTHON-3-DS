# Importa a biblioteca Tkinter e cria o apelido "tk"
import tkinter as tk

# Classe principal da calculadora
class Calculadora:

    # Método executado automaticamente ao criar a calculadora
    def __init__(self, root):

        # Guarda a janela principal
        self.root = root

        # Título da janela
        self.root.title("Calculadora Moderna")

        # Define largura x altura
        self.root.geometry("360x550")

        # Define a cor de fundo da janela
        self.root.configure(bg="#1e1e1e")

        # Impede redimensionamento da janela
        self.root.resizable(False, False)

        # Variável que armazenará a operação digitada
        self.expressao = ""

        # ==========================
        # DISPLAY DA CALCULADORA
        # ==========================

        self.display = tk.Entry(
            root,
            font=("Segoe UI", 24, "bold"), # Fonte
            bd=0,                          # Remove borda
            bg="#252526",                # Cor de fundo
            fg="white",                    # Cor do texto
            justify="right",               # Alinha texto à direita
            insertbackground="white"       # Cor do cursor
        )

        # Posiciona o display
        self.display.pack(
            fill="both",
            padx=10,
            pady=15,
            ipady=20
        )

        # ==========================
        # FRAME DOS BOTÕES
        # ==========================

        frame = tk.Frame(
            root,
            bg="#1e1e1e"
        )

        frame.pack(
            expand=True,
            fill="both",
            padx=10,
            pady=10
        )

        # ==========================
        # DEFINIÇÃO DOS BOTÕES
        # ==========================

        botoes = [
            ["C", "<=", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        # Percorre cada linha da lista
        for linha in botoes:

            # Cria um frame para cada linha de botões
            row_frame = tk.Frame(
                frame,
                bg="#1e1e1e"
            )

            row_frame.pack(
                expand=True,
                fill="both"
            )

            # Percorre cada botão da linha
            for texto in linha:

                # Cor padrão dos botões numéricos
                cor = "#3a3d41"
                fg = "white"

                # Operadores ficam azuis
                if texto in ["+", "-", "*", "/", "="]:
                    cor = "#0078D7"

                # Botão limpar fica vermelho
                if texto == "C":
                    cor = "#D83B01"

                # Botão apagar fica cinza
                if texto == "<=":
                    cor = "#605E5C"

                # Botão porcentagem fica verde
                if texto == "%":
                    cor = "#107C10"

                # Cria o botão
                botao = tk.Button(
                    row_frame,
                    text=texto,
                    font=("Segoe UI", 18, "bold"),
                    bg=cor,
                    fg=fg,
                    bd=0,
                    activebackground="#505050",
                    activeforeground="white",
                    cursor="hand2",
                    
                    height=2,
                    width=4,

                    # Envia para a função clique()
                    command=lambda t=texto: self.clique(t)
                )

                # Posiciona o botão
                botao.pack(
                    side="left",
                    expand=True,
                    fill="both",
                    padx=4,
                    pady=4
                )

                # ==========================
                # EFEITO HOVER
                # ==========================

                # Quando o mouse entra
                botao.bind(
                    "<Enter>",
                    lambda e, b=botao: b.config(bg="#606060")
                )

                # Quando o mouse sai
                botao.bind(
                    "<Leave>",
                    lambda e, b=botao, c=cor: b.config(bg=c)
                )

    # ==========================
    # TRATAMENTO DOS CLIQUES
    # ==========================
    def clique(self, valor):

        # Botão Limpar
        if valor == "C":

            # Esvazia a expressão
            self.expressao = ""

        # Botão apagar último caractere
        elif valor == "<=":

            # Remove o último caractere
            self.expressao = self.expressao[:-1]

        # Botão igual
        elif valor == "=":

            try:
                # Calcula a expressão digitada
                self.expressao = str(
                    eval(self.expressao)
                )

            except:
                # Caso ocorra erro
                self.expressao = "Erro"

        # Botão porcentagem
        elif valor == "%":

            try:
                # Divide por 100
                self.expressao = str(
                    float(self.expressao) / 100
                )

            except:
                self.expressao = "Erro"

        # Qualquer outro botão
        else:

            # Adiciona à expressão
            self.expressao += valor

        # Atualiza o display
        self.atualizar_display()

    # ==========================
    # ATUALIZA O DISPLAY
    # ==========================
    def atualizar_display(self):

        # Limpa o display
        self.display.delete(0, tk.END)

        # Exibe o conteúdo da expressão
        self.display.insert(
            0,
            self.expressao
        )

# ==========================
# INÍCIO DO PROGRAMA
# ==========================

# Cria a janela principal
root = tk.Tk()

# Cria o objeto da calculadora
app = Calculadora(root)

# Mantém a janela aberta
root.mainloop()