# ESCREVA UM PROGRAMA QUE DEFINA UMA FUNÇÃO, QUE CALCULE A [AREA DE UM RETÂNGULO ( BASE X ALTURA )] E IMPRIMA A ÁREA DO RETÂNGULO.
def area_retangulo(base, altura):
    area = base * altura
    return area 
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = area_retangulo(base, altura)
print(f"A área do retângulo é: {area}")