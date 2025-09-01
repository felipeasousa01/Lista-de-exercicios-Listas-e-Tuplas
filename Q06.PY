# Peça ao usuário para inserir 5 números em uma lista e calcule a soma total.
numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
soma = sum(numeros)
print("A soma total dos números é:", soma)