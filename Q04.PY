# 04- Peça ao usuário para digitar 5 números e armazene-os em uma lista. Depois exiba a lista completa
numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
print("A lista completa de números é:", numeros)