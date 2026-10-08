import tkinter as tk
from tkinter import tk, messagebox

# Banco de dados em memória

produtos = []
clientes = []
fornecedores = []

# Máscaras

def mascara_cpf(event, var):
    cpf = "".join(filter(str.isdigit, var.get()))
    cpf = cpf[:11]

    if len(cpf) <= 3:
        texto = cpf
    elif len(cpf) <= 6:
        texto = f"{cpf[:3]}.{cpf[3:]}"
    elif len(cpf) <= 9:
        texto = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}"
    else:
        texto = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}-{cpf[9:]}"

    var.set(texto)

def mascara_cnpj(event, var):
    cnpj = "".join(filter(str.isdigt, var.get()))
    cnpj = cnpj[:14]

    if len(cnpj) <= 2:
        texto = cnpj
    elif len(cnpj) <= 5:
        texto = f"{cnpj[:2]}.{cnpj[2:]}"
    elif len(cnpj) <= 8:
        texto = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:]}"
    elif len(cnpj) <= 13:
        texto = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}.{cnpj[8:]}"
    else:
        texto = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}.{cnpj[8:12]}-{cnpj[12:]}"

    var.set(texto)

def mascara_telefone(event, var):
    telefone = "".join(filter(str.isdigt, var.get()))
    telefone = telefone[:11]

    if len(telefone) <= 2:
        texto = telefone
    elif len(telefone) <= 7:
        texto = f"({telefone[:2]}) {telefone[2:]}"
    else:
        texto = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"

    var.set(texto)

# Produtos

def tela_produtos():
    janela = tk.Toplevel(root)
    janela.title("Cadastro de Produtos")
    janela.geometry("400x300")

    tk.Label(janela, text="Nome do Produto *").pack(pady=5)
    nome = tk.Entry(janela, width=40)
    nome.pack()