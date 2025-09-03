# 15- Crie uma tupla com números e verifique se um número digitado pelo usuário está dentro da tupla.
tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numero_usuario = int(input("Digite um número para verificar se está na tupla: "))
if numero_usuario in tupla_numeros:
    print(f"O número {numero_usuario} está na tupla.")
else:
    print(f"O número {numero_usuario} não está na tupla.")  