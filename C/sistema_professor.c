#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

#define MAX_ALUNOS 40 // fixa o tamanho máximo

struct Aluno {
    char nome[50];
    char matricula[20];
    float p1, p2, trab;
    int presentes;
    int totalAulas;
    float media;
    float freq;
};

struct Turma {
    struct Aluno alunos[MAX_ALUNOS];
    int qtd;
    char nomeTurma;
};

// função para calcular média
float calcularMedia(float p1, float p2, float trab) {
    return (p1 + p2 + trab) / 3;
}

// função para calcular frequência
float calcularFreq(int presentes, int totalAulas) {
    if (totalAulas == 0) return 0;
    return (presentes * 100.0) / totalAulas;
}

// função para limpar a tela
void limpar() {
    system("cls");
}

// função para pausar o sistema
void pausar() {
    system("pause");
}

int main(void) {
	setlocale(LC_ALL, "Portuguese");
	
	struct Turma turmaA, turmaB;
	turmaA.qtd = 0; // iniciando com as turmas vazias
	turmaB.qtd = 0;
	
	int opcDisciplina;
	int continuarGeral = 1;
	
	char disciplinas[5][30] = {
	    "Português", "Matemática", "História", "Biologia", "Filosofia"
	};

	while (continuarGeral) { // loop principal do programa
	    limpar();
        printf("SISTEMA DE NOTAS E FREQUÊNCIAS\n");

        printf("\nSelecione a disciplina:\n");
        printf("[1] Português\n");
        printf("[2] Matemática\n");
        printf("[3] História\n");
        printf("[4] Biologia\n");
        printf("[5] Filosofia\n\n");
        printf("Escolha: ");
        scanf("%d", &opcDisciplina);
        
        if (opcDisciplina < 1 || opcDisciplina > 5) {
            printf("\nOpção inválida! Selecione um número de 1 a 5\n");
            pausar();
            continue;
        }
        
        char disciplinaAtual[30];
        strcpy(disciplinaAtual, disciplinas[opcDisciplina - 1]);

	    char primeiraTurma;
        char segundaTurma;
        char ordem[2];

        // Escolhendo qual turma iniciar - A ou B
        while (1) {
            limpar();
            printf("DISCIPLINA: %s\n\n", disciplinaAtual);
            printf("Qual turma deseja cadastrar primeiro?\n");
            printf("[A] Turma A\n");
            printf("[B] Turma B\n\n");
            printf("Escolha (letra maiúscula): ");
            scanf(" %c", &primeiraTurma); 
	    
	    	if (primeiraTurma == 'A' || primeiraTurma == 'B') {
                break;
            } else {
                printf("\nOpção inválida! Digite A ou B.\n");
                pausar();
            }	    
		}
		
		// definindo a outra turma automaticamente
        if (primeiraTurma == 'A') {
            segundaTurma = 'B';
        } else {
            segundaTurma = 'A';
        }

        ordem[0] = primeiraTurma;
        ordem[1] = segundaTurma;
	
		int rodada;
		// for simples que roda duas vezes: primeiraTurma, depois segundaTurma
        for (rodada = 0; rodada < 2; rodada++) { // rodada 0 = primeira turma / rodada 1 = segunda turma
        
            char turmaAtualLetra = ordem[rodada];
            struct Turma turmaAtual; // criamos uma variável temporária para facilitar

            if (turmaAtualLetra == 'A') turmaAtual = turmaA;
            else turmaAtual = turmaB;

            // garantindo que nomeTurma esteja certo
            turmaAtual.nomeTurma = turmaAtualLetra;
            
            int continuarCadastro = 1;
            
            while (continuarCadastro) {
                limpar();
                printf("DISCIPLINA: %s\n", disciplinaAtual);
                printf("Cadastro de aluno - Turma %c\n", turmaAtual.nomeTurma);

                struct Aluno novo;

                printf("\nDigite o nome do aluno: ");
                scanf(" %[^\n]", novo.nome);

                printf("\nDigite a matrícula do aluno: ");
                scanf("%s", novo.matricula);

                printf("\nDigite a nota da prova 1: ");
                scanf("%f", &novo.p1);

                printf("Digite a nota da prova 2: ");
                scanf("%f", &novo.p2);

                printf("Digite a nota do trabalho: ");
                scanf("%f", &novo.trab);

                printf("\nDigite o número de aulas presentes: ");
                scanf("%d", &novo.presentes);

                printf("Digite o total de aulas: ");
                scanf("%d", &novo.totalAulas);

                //calculando média e frequência
                novo.media = calcularMedia(novo.p1, novo.p2, novo.trab);
                novo.freq = calcularFreq(novo.presentes, novo.totalAulas);

                //adicionando aluno à turma
                turmaAtual.alunos[turmaAtual.qtd] = novo;
                turmaAtual.qtd++;

                //mostra o resultado do aluno
                printf("\nMédia do aluno: %.2f\n", novo.media);
                printf("Frequência: %.1f%%\n", novo.freq);

                int opc;
                printf("\nDeseja cadastrar outro aluno? [1-Sim / 2-Relatório]: ");
                scanf("%d", &opc);
                if (opc == 2) {
                	continuarCadastro = 0;
				
				
	                // relatório da turma
		            limpar();
		            printf("RELATÓRIO TURMA %c\n", turmaAtual.nomeTurma);
		            printf("Disciplina: %s\n\n", disciplinaAtual);
		
		            float somaMedias = 0;
		            int i;
		            for (i = 0; i < turmaAtual.qtd; i++) {
		                struct Aluno a = turmaAtual.alunos[i];
		                printf("Nome: %s\n", a.nome);
		                printf("Matrícula: %s%c\n", a.matricula, turmaAtual.nomeTurma);
		                printf("Média: %.2f\n", a.media);
		                printf("Frequência: %.1f%%\n", a.freq);
		                printf("-----------------------------\n");
		                somaMedias += a.media;
		            }
		
		            float mediaGeral = (turmaAtual.qtd > 0) ? somaMedias / turmaAtual.qtd : 0;
		            printf("MÉDIA GERAL DA TURMA %c: %.2f\n", turmaAtual.nomeTurma, mediaGeral);
		            pausar();
		    	}
				
	
		            // salva dados de volta na turma correta
		            if (turmaAtual.nomeTurma == 'A') turmaA = turmaAtual;
		            else turmaB = turmaAtual;
				}
	    } //fechamento do for rodada
	        
	    // comparação entre turmas
	    float somaA = 0, somaB = 0;
	    int i;
	    for (i = 0; i < turmaA.qtd; i++) somaA += turmaA.alunos[i].media;
	    for (i = 0; i < turmaB.qtd; i++) somaB += turmaB.alunos[i].media;
	
	    float mediaA = (turmaA.qtd > 0) ? somaA / turmaA.qtd : 0;
	    float mediaB = (turmaB.qtd > 0) ? somaB / turmaB.qtd : 0;
	
	    limpar();
	    printf("COMPARAÇÃO ENTRE TURMAS\n");
	    printf("Média geral Turma A: %.2f\n", mediaA);
	    printf("Média geral Turma B: %.2f\n", mediaB);
	
	    if (mediaA > mediaB) printf("\nA Turma A teve melhor rendimento.\n");
	    else if (mediaB > mediaA) printf("\nA Turma B teve melhor rendimento.\n");
	    else printf("\nAs duas turmas tiveram o mesmo rendimento.\n");
	
	    pausar();
	
	    // resetar turmas para nova disciplina
	    turmaA.qtd = 0;
	    turmaB.qtd = 0;
	                              
	                
    } //fechamento do loop (while) principal
                   
} // fechamento do main
