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
            veiculo.disponive = False
            self.locacoes[placa] = cpf
            return f"Veiculo {Veiculo.modelo} alugado para {cliente.nome}."
        return "Erro ao alugar veículo. Verifique os dados."