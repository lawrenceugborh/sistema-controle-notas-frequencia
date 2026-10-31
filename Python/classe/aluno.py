class Aluno:
    def __init__(self, nome, matricula, nota1, nota2, trabalho, presencas, total_aulas):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.trabalho = trabalho
        self.presencas = presencas
        self.total_aulas = total_aulas

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.trabalho) / 3
    
    def calcular_frequencia(self):
        if self.total_aulas == 0:
            return 0
        else: 
            return (self.presencas / self.total_aulas) * 100
