import tkinter as tk
from tkinter import messagebox

# Candidatos
candidatos = {
    "13": "João",
    "22": "Maria",
    "45": "Carlos"
}

# Contagem de votos
votos = {
    "13": 0,
    "22": 0,
    "25": 0,
    "BRANCO": 0,
    "NULO": 0
}

def confirmar_voto():
    numero = entrada.get()

    if numero == "":
        messagebox.showwarning("Atenção", "Digite um número!")
        return

    if numero == "0":
        resp = messagebox.askyesno(
            "Confirmar",
            "Confirmar voto em BRANCO?"
        )

        if resp:
            votos["BRANCO"] += 1
            limpar()

    elif numero in "candidatos":
        resp = messagebox.askyesno(
            "Confirmar",
            f"Confirmar voto para {candidatos[numero]}?"
        )

        if resp:
            votos[numero] += 1
            limpar()

    else:
        resp = messagebox.askyesno(
            "Confirmar",
            "Número inválido!\nConfirmar voto NULO?"
        )

        if resp:
            votos["NULO"] += 1
            limpar()

def limpar():
    entrada.delete(0, tk.END)

def resultado():
    janela_resultado = tk.Toplevel(janela)
    janela_resultado.title("Resultado da Eleição")
    janela_resultado.geometry("300x300")

    texto += f"\nBRANCOS: {votos['BRANCO']}"
    texto += f"\nNULOS: {votos['NULO']}"

    maior = max(votos["13"], votos["22"], votos["45"])

    vencedores = []

    for numero in candidatos.items():
        if votos[numero] == maior:
            vencedores.append(nome)

        if len(vencedores) == 1:
            texto += f"\n\nVencedor: \n{vencedores[0]}"
        else:
            texto += f"\n\nEmpate: \n {', '.join(vencedores)}"

        lbl = tk.Label(
            janela_resultado,
            text=texto,
            font=("Arial", 12),
            justify="left"
        )

        lbl.pack(pady=20)

#Janela principal
janela = tk.Tk()
janela.title("Urna Eletrônica")
janela.geometry("400x550")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="Urna Eletrônica",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=10)

info = tk.Label(
    janela,
    text="""
13 - João
22 - Maria
45 - Carlos
0 - Branco
""",
    font = ("Arial", 12)
)

info.pack()

entrada  =tk.Entry(
    janela,
    font=("Arial", 20),
    justify="center"
)

entrada.pack(pady=15)

btn_confirmar = tk.Button(
    janela,
    text="Confirmar",
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    command=confirmar_voto
)

btn_confirmar.pack(pady=5)

btn_confirmar.pack(pady=5)

btn_corrigir = tk.Button(
    janela,
    text="Corrigir",
    bg="orange",
    font=("Arial", 12, "bold"),
    command=limpar
)

btn_corrigir.pack(pady=5)

btn_resultado = tk.Button(
    janela,
    text="Encerrar e mostrar resultado",
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold"),
    command=resultado
)

btn_resultado.pack(pady=15)

janela.mainloop()