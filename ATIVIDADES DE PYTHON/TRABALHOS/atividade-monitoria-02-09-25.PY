# LISTA DA MONITORIA

#QUESTAO 1 - Faça um Programa que leia 5 números inteiros, armazene-os em
for i in range(5):
    n = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(n)

print("Lista de números:", numeros)

#QUESTAO 2 - Faça um Programa que leia 10 números reais e mostre-os na ordem inversa.
numeros_10 = []
for i in range (10):
 	 	numero = int(input(f"Digite o número {i+1}: "))
  		numeros_10.append(numero)
numeros_10.sort(reverse=True)
print(f"Os números na ordem invertida são: \n{numeros_10}")

#QUESTAO 3 - Faça um Programa que leia 40 notas, mostre as notas e a média na tela.
notas = []
for i in range(4):
    n = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(n)


media = sum(notas) / len(notas)


print("Notas:", notas)
print("Média:", media)

#QUESTAO 4 - Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima as três listas.
numeros = []
pares = []
impares = []


for numero in range(1, 21):
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)


print(f"lista dos numero {numeros}")
print(f"lista dos pares {pares}")
print(f"lista dos impares {impares}")

#QUESTAO 5 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
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

#QUESTAO 6 - Faça um Programa que leia e armazene 50 números inteiros, mostre a soma, a multiplicação e os números
num = []
mult = 1

for i in range(50):  # lê 50 números
    numero = int(input(f"Digite o {i+1}º número: "))
    num.append(numero)
    mult *= numero

soma = sum(num)  # calcula a soma após o loop

print(f"Números: {num}")
print(f"Soma: {soma}")
print(f"Multiplicação: {mult}")

#7 Faça um Programa que peça a idade e a altura de 10 pessoas, armazene cada informação na sua respectiva lista. Imprima a idade da pessoa que possui maior altura.
idades = []
alturas = []


for i in range(10):
    print("Pessoa", i + 1)
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (em metros): "))

    idades.append(idade)
    alturas.append(altura)


maior_altura = max(alturas)
indice = alturas.index(maior_altura)
print("A maior altura foi: ", maior_altura)
print("A idade mais alta foi: ", idades[indice])

#8 - Faça um Programa que leia uma lista A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
# Lendo a lista A com 10 números inteiros
A = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    A.append(num)
# Calculando a soma dos quadrados
soma_quadrados = 0
for num in A:
    soma_quadrados += num ** 2
# Mostrando o resultado
print("A soma dos quadrados dos elementos é:", soma_quadrados)

#9 - Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas.
# Criar duas listas
lista1 = []
lista2 = []

print("Digite 10 números para a primeira lista:")
for i in range(10):
    lista1.append(int(input(f"Número {i+1}: ")))

print("\nDigite 10 números para a segunda lista:")
for i in range(10):
    lista2.append(int(input(f"Número {i+1}: ")))

# Criar lista intercalada
lista3 = []
for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

# Mostrar resultado
print("\nPrimeira lista:", lista1)  
print("\nSegunda lista:",lista2)
print("\nLista intercalada com 20 elementos:")
print(lista3)

#10 - Altere o programa anterior, intercalando.
