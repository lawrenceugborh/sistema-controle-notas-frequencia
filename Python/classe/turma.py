# criando uma classe para turma
class Turma:
    def __init__(self, letra):
        self.letra = letra # turma "A" ou "B"
        self.lista_estudantes = [] # lista para guardar os objetos da classe Aluno
        self.media_geral = 0 
    
    def adicionar_aluno(self, novo_aluno):
            #Recebe um objeto da classe Aluno e adiciona à turma
            self.lista_estudantes.append(novo_aluno)
            print(f"Aluno {novo_aluno.nome} cadastrado na turma {self.letra} com sucesso!")

    def listar_alunos(self):
            #Lista todos os alunos com médias e frequência.
            if not self.lista_estudantes:
                print(f"A turma {self.letra} ainda não possui alunos cadastrados.")
                return
            
            #"aluno" é uma variável local
            print(f"\n=== Alunos da turma {self.letra} ===")
            for aluno in self.lista_estudantes:
                print(f"Nome: {aluno.nome} | Matrícula: {aluno.matricula}")
                print(f"Média: {aluno.calcular_media():.2f}")
                print(f"Frequência: {aluno.calcular_frequencia():.1f}%")
                print("-----------------------------")
    
    def calcular_media_geral(self):
            #Calcula a média geral da turma.
            if not self.lista_estudantes:
                self.media_geral = 0
                return 0
            
            soma_medias = sum(aluno.calcular_media() for aluno in self.lista_estudantes)
            self.media_geral = soma_medias / len(self.lista_estudantes)
            return self.media_geral
    
    def calcular_media_geral(self):
            #Calcula a média geral da turma.
            if not self.lista_estudantes:
                self.media_geral = 0
                return 0
            
            soma_medias = sum(aluno.calcular_media() for aluno in self.lista_estudantes)
            self.media_geral = soma_medias / len(self.lista_estudantes)
            return self.media_geral

    def gerar_relatorio(self):
        #Mostra a média geral e informações básicas da turma.
        print(f"\n=== Relatório da Turma {self.letra} ===")

        if not self.lista_estudantes:
            print("Nenhum aluno cadastrado ainda.")
            return

        media = self.calcular_media_geral()

        print(f"Total de alunos: {len(self.lista_estudantes)}")
        print(f"Média geral da turma: {media:.2f}")
        print("==============================")

    
    
   