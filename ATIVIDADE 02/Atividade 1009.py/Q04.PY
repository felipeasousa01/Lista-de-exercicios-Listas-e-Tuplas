# Crie uma função que mostre a tabuada de um número.
def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}") 
# Programa principal
n = int(input("Digite um número para ver a tabuada: "))
tabuada(n)