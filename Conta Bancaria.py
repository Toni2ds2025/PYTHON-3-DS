class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, cliente, numero_cliente, saldo=0):
        self.cliente = cliente
        self.numero_cliente = numero_cliente
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R$ {valor:.2f} realizado.")
        else:
            print("Valor inválido!")

    def sacar(self, valor):
        if self.saldo >= valor and valor > 0:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Saldo insuficiente!")

    def exibir_saldo(self):
        print(f"Saldo atuall: R${self.saldo:.2f}.")

#Criando os objetos
cliente1 = Cliente("Ana", "123.456.789-00", "Rua A, 123")
conta1 = ContaBancaria(cliente1, "12345-6")

#Operações na conta
print("-" *20)
conta1.depositar(1000)
print("-" *20)
conta1.sacar(500)
print("-" *20)
conta1.exibir_saldo()