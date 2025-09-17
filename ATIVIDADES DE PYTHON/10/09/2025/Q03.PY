# Crie uma função que receba uma lista de números e retorne a soma.
def soma(numeros):
    return sum(numeros)
# Programa principal

n = int(input("Quantos números você quer somar? "))
lista = []
for i in range(n):
    num = float(input(f"Digite o número {i+1}: "))
    lista.append(num)   
resultado = soma(lista)
print("A soma dos números é:", resultado)