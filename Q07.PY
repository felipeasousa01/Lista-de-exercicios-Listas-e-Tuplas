# 07- insira 05 inteiros em uma lista e exiba o maior e o menor valor.
numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
print(" O maior número é:", max(numeros))
print(" O menor número é:", min(numeros))


