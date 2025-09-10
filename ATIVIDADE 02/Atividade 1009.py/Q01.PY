# Crie uma função que receba um número e retorne o seu quadrado.

def quadrado(numero):
    return numero * numero

# Programa principal
n = int(input("Digite um número: "))
resultado = quadrado(n)
print("O quadrado de", n, "é", resultado)
