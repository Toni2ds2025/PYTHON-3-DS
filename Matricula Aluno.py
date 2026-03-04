class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = {}     # Dicionario para armazenar notas por disciplina

    def adicionar_nota(self, disciplina, nota):
        self.notas[disciplina] = nota
    
    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas.values()) / len(self.notas)

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Matricula: {self.matricula}")
        print(f"Curso: {self.curso}")
        print("Notas: ")
        for disciplina, nota in self.notas.items():
            print(f" {disciplina}: {nota}")
        print(f"Média: {self.calcular_media():.2f}")

# Criando objetos alunos
aluno1 = Aluno("João", "202312345", "Engenharia")
aluno2 = Aluno("Maria", "202367890", "Ciências da Computação")

#Adicionando notas
aluno1.adicionar_nota("Matemática", 8.5)
aluno1.adicionar_nota("Física", 7.0)
aluno2.adicionar_nota("Programação", 9.0)
aluno2.adicionar_nota("Banco de Dados", 8.0)

#Exibindo informações
aluno1.exibir_informacoes()
print("-" * 20)
aluno2.exibir_informacoes()
print("-" * 20)