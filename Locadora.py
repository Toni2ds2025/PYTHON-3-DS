import tkinter as tkinter
from tkinter import messagebox, simpledatalog

class Veiculo:
    def __init__(self, placa, madelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Alugado"
        return f"{self.modelo} ({self.ano}) - Placa: {self.placa} - {status}"

class Cliente:
    def __init__(self):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"

class Locadora:
    def __init__(self):
        self.veiculos = []
        self.clientes = []
        self.locacoes = []

    def cadastrar_veiculos(self, veiculo):
        self.veiculos.append(veiculo)

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def alugar_veiculo(self, cpf, placa):
        cliente = next((c for c in self.clientes if c.cpf == cpf), None)
        cliente = next((v for v in self.veiculos if v.placa == placa), None)

        if cliente and veiculo and veiculo.disponivel:
            veiculo.disponivel = False
            self.locacoes[placa] = cpf
            return f"Veiculo {Veiculo.modelo} alugado para {cliente.nome}."
        return "Erro ao alugar veículo. Verifique os dados."
    
    def devolver_veiculo(self, placa):
        veiculo = next((v for v in self.veiculos if v.placa == placa), None)
    
        if veiculo and not veiculo.disponivel:
            veiculo.disponivel = True
            self.locacoes.pop(placa, None)
            return f"Veiculo {veiculo.modelo} devolvido com sucesso."
        return "Erro ao devolver veiculo. Verifique os dados."
    
    def listar_veiculos(self, disponiveis=True):
        return [str(v) for v in self.veiculos if v.disponivel == disponiveis]
    
class App:
    def __init__(self, root):
        self.locadora = Locadora()
        self.root = root
        self.root.title("Locadora de veiculos")

        tk Button(root, text="Cadastrar Veiculos", command=self.cadastrar_veiculo).pack(fill='x')
        tk Button(root, text="Cadastrar Cliente", command=self.cadastrar_cliente).pack(fill='x')
        tk Button(root, text="Alugar Veiculo", command=self.alugar_veiculo).pack(fill='x')
        tk Button(root, text="Devolver Veiculos", command=self.devolver_veiculo).pack(fill='x')
        tk Button(root, text="Listar Veiculos Disponíveis", command=self.listar_alugados).pack(fill='x')
        tk Button(root, text="Listar Veiculos Alugados", command=self.listar_alugados).pack(fill='x')

    def cadastrar_veiculo(self):
        placa = simpledatalog.askstring("Cadastro", "Placa:")
        modelo = simpledatalog.askstring("Cadastro", "Modelo:")
        ano = simpledatalog.askstring("Cadastro", "Ano:")
        if placa and modelo and ano:
            self.locadora.cadastrar_veiculo(Veiculo(placa, modelo, ano))
            messagebox.showinfo("Sucesso", "Veiculo cadastrado!")

    def cadastrar_cliente(self):
        nome = simpledatalog.askstring("Cadastro", "Nome:")
        cpf = simpledatalog.askstring("Cadastro", "CPF:")
        if nome and cpf:
            self.locadora.cadastrar_cliente(Cliente(nome, cpf))
            messagebox.showinfo("Sucesso", "Cliente cadastrado!")