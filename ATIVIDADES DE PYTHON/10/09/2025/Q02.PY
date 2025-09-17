# Crie uma função que receba dois números e retorne o maior deles.
def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
# Programa principal
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
resultado = maior_numero(n1, n2)
print("O maior número é:", resultado)   
