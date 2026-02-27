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
        return sum(self.notas.value()) / len(self.notas)

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Matricula: {self.matricula}")
        print(f"Curso {self.curso}")
        print("Notas: ")