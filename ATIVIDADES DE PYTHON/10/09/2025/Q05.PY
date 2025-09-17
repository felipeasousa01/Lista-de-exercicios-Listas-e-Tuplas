# Use lambda para criar uma função que calcule o dobro de um número.
dobro = lambda x: x * 2
# Programa principal
n = float(input("Digite um número: "))
resultado = dobro(n)
print("O dobro de", n, "é", resultado)  