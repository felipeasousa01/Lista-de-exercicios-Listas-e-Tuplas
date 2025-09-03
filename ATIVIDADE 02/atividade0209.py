# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
medias = []
for i in range(10):
    print(f"Aluno {i+1}:")
    notas = []
    for j in range(4):
        nota= float(input(f"Digite a nota {j+1}:"))
        notas.append(nota)
        media = sum(notas)/4
        medias.append(media)

        # conta-se quantos possuem média maior ou igual a 7
        aprovados = 0
        for media in medias:
            if media >= 7:
                aprovados +=1

    print("Número de alunos com média maior ou igual a7.0:", aprovados)