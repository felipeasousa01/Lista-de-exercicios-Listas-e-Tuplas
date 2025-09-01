# 10- Peça ao usuário um número N e crie uma lista com todos os números pares de 1 até N.
N = int(input("Digite um número N: "))
pares = []
for i in range(1, N + 1):
    if i % 2 == 0:
        pares.append(i)
print("Números pares de 1 até", N, ":", pares)
