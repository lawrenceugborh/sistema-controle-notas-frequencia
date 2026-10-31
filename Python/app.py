import os
from classe.aluno import Aluno
from classe.turma import Turma

def limpar_tela():
    os.system('cls')

turmaA = Turma("A")
turmaB = Turma("B")


# criando um dicionário para as disciplinas 
disciplinas = {
    1: "Português",
    2: "Matemática",
    3: "História",
    4: "Biologia",
    5: "Filosofia"
}

while True:
     # SE FOR PRIMEIRA EXECUÇÃO - Mostra menu
    print("Sistema de Controle de Notas e Frequência para Professores")
    print("Selecione a disciplina:")
    for numero, nome in disciplinas.items():
        print(f'{numero} - {nome}')

    opcao = int(input('Escolha a disciplina (1 a 5): '))
    limpar_tela()
    if opcao < 1 or opcao > 5:
        print("Opção inválida! Você deve digitar um número entre 1 e 5.")
        os.system("pause")
        limpar_tela()
        continue

    #Salvando o nome da disciplina - será mostrado mais a frente
    disciplina_escolhida = disciplinas[opcao]
    
    #Selecionando a turma
    print("Selecione a turma:")
    print("A - Turma A")
    print("B - Turma B")
    turma_escolhida = input("Opção: ")

    limpar_tela()

    if turma_escolhida == "A":
        turma_atual = turmaA
        proxima_turma = turmaB
    elif turma_escolhida == "B":
        turma_atual = turmaB
        proxima_turma = turmaA
    else:
        print("Opção inválida!")
        os.system("pause")
        limpar_tela()
        continue

    # LOOP PARA CADASTRAR AS DUAS TURMAS SEM VOLTAR AO MENU
    while True:

        #2a TELA! - Cadastro dos alunos
        while True:
            print("Cadastro do aluno(a)")
            print(f"Disciplina selecionada: {disciplina_escolhida}\n")
            nome = input("Digite o nome do aluno(a): ")
            matricula = input("Digite a matrícula: ")
            matricula = matricula + turma_atual.letra.lower()

            
            print("\nCalculando a média:")
            nota1 = float(input("Insira a nota da prova 1: "))
            nota2 = float(input("Insira a nota da prova 2: "))
            trabalho = float(input("Insira a nota do trabalho: "))

            presencas = int(input("\nInsira o número de aulas comparecidas: "))
            total_aulas = int(input("Insira o número total de aulas realizadas: "))

            #criando o objeto
            novo_aluno = Aluno(nome, matricula, nota1, nota2, trabalho, presencas, total_aulas)

            #Calculando média e frequência
            media_aluno = novo_aluno.calcular_media()
            frequencia_aluno = novo_aluno.calcular_frequencia()

            #Exibindo os resultados
            print(f"\nMédia do aluno: {media_aluno:.2f}")
            print(f"Frequência: {frequencia_aluno:.1f}%")

            #Adicionando à turma
            turma_atual.adicionar_aluno(novo_aluno)

            print("\nO que deseja fazer?")
            print("1 - Cadastrar outro aluno")
            print("2 - Ir para relatório da turma")
            opcao_relatorio = input("Opção: ")

            limpar_tela()

            if opcao_relatorio == "2":
                break  # Sai do cadastro e vai para relatório

        # RELATÓRIO DA TURMA
        print(f"RELATÓRIO DA TURMA {turma_atual.letra}\n")
        print(f"Disciplina selecionada: {disciplina_escolhida}\n")
        for aluno in turma_atual.lista_estudantes:
            print(f"Nome: {aluno.nome}")
            print(f"Matrícula: {aluno.matricula}")
            print(f"Média: {aluno.calcular_media():.2f}")
            print(f"Frequência: {aluno.calcular_frequencia():.1f}%")
            print("-" * 30)

        #média geral da turma 
        medias = [aluno.calcular_media() for aluno in turma_atual.lista_estudantes]
        media_geral = sum(medias) / len(medias) if medias else 0

        print(f"MÉDIA GERAL DA TURMA {turma_atual.letra}: {media_geral:.2f}\n")

        # SE ESTA FOI A PRIMEIRA TURMA - VAI PARA A PRÓXIMA AUTOMATICAMENTE
        if turma_atual == proxima_turma:
            break  # Já cadastrou A e B - sai

        # Definir qual é a próxima turma a cadastrar
        if turma_atual.letra == "A":
            proxima_turma = turmaB
        else:
            proxima_turma = turmaA

        print(f"Agora você será direcionado para cadastrar a Turma {proxima_turma.letra}...")
        os.system("pause")
        limpar_tela()

        # Troca automática — SEM passar pela seleção de disciplina/turma
        turma_atual = proxima_turma
        continue   # volta direto para o cadastro da próxima turma
    
    #COMPARAÇÃO FINAL ENTRE AS TURMAS
    os.system("pause")
    limpar_tela()

    mediasA = [a.calcular_media() for a in turmaA.lista_estudantes]
    mediasB = [a.calcular_media() for a in turmaB.lista_estudantes]

    mediaA = sum(mediasA) / len(mediasA) if mediasA else 0
    mediaB = sum(mediasB) / len(mediasB) if mediasB else 0

    print("COMPARAÇÃO ENTRE TURMAS\n")
    print(f"Média geral Turma A: {mediaA:.2f}")
    print(f"Média geral Turma B: {mediaB:.2f}")

    if mediaA > mediaB:
        print("\nA Turma A teve melhor rendimento.")
    elif mediaB > mediaA:
        print("\nA Turma B teve melhor rendimento.")
    else:
        print("\nAs duas turmas tiveram o mesmo rendimento.")

    os.system("pause")
    limpar_tela()

    #RESETANDO as turmas para começar um novo ciclo    
    turmaA = Turma("A")
    turmaB = Turma("B")

    #Voltar para o início do programa
    continue