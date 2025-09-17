## ATIVIDADE IMC ##

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

# Calculadora de IMC
print("=== Calculadora de IMC ===")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

resultado = calcular_imc(peso, altura)
print("Seu IMC é:", round(resultado))



def quadrado(numero):
    return numero * numero

# Programa principal
n = int(input("Digite um número: "))
resultado = quadrado(n)
print("O quadrado de", n, "é", resultado)
