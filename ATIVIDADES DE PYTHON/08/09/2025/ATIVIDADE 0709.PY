# 1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
livros = ["Harry Potter", "Os mentirosos", "Silêncio dos inocentes"]
print(livros)

# 2- Usando a lista livros, exiba apenas o primeiro e o último elemento.
print("Primeiro livro:", livros[0])
print("Último livro:", livros[-1])

# 3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros.append("Os miseráveis")
livros.append("Percy Jackson")
print(livros)

# 4- Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros.insert(1, "Duna")
print(livros)

# 5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
else:
    print("Livro não encontrado")
print(livros)

# 6- Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.
numeros = [1, 2, 3, 2, 4, 2, 5]
print("O número 2 aparece", numeros.count(2), "vezes")

# 7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
for livro in livros:
    print("O livro", livro, "é interessante")

# 8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
idades = [12, 18, 25, 14, 30]

for idade in idades:
    if idade >= 18:
        print(idade)

# 9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.
valores = [10, 20, 30, 40]
soma = 0

for v in valores:
    soma = soma + v

print("Soma dos valores:", soma)

# 10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
# notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.
notas = []

for i in range(2):
    aluno = []
    print("Digite as 3 notas do aluno", i+1)
    for j in range(3):
        n = float(input("Nota: "))
        aluno.append(n)
    notas.append(aluno)

print("Notas:", notas)

for i in range(len(notas)):
    media = sum(notas[i]) / len(notas[i])
    print("Média do aluno", i+1, ":", media)

# 11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:
#               [ ] - para posições vazias
#                    tor - para a torre
#                    cav - para o cavalo
#                    bis - para o bispo
#                    rai - para a rainha
#                    rei - para o rei
#                    pea - para o peão

# Cria tabuleiro vazio
tabuleiro = [["[ ]" for i in range(8)] for j in range(8)]

# Peças pretas
tabuleiro[0] = ["tor", "cav", "bis", "rei", "rai", "bis", "cav", "tor"]
tabuleiro[1] = ["pea"] * 8

# Peças brancas
tabuleiro[6] = ["pea"] * 8
tabuleiro[7] = ["tor", "cav", "bis", "rei", "rai", "bis", "cav", "tor"]

# Imprimir tabuleiro
for linha in tabuleiro:
    print(linha)

