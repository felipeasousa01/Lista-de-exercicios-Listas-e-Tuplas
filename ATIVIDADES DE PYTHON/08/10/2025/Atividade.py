#ATIVIDADE 08/10/2025

# RESPOSTAS
#1. A programação estrutural organiza o código em funções e blocos de instruções, enquanto a orientada a objetos (POO) organiza o código em classes e objetos. Na POO, juntamos dados e comportamentos no mesmo lugar (objeto), o que facilita a reutilização e manutenção.

#2. A Saída será: 4 4 4
#Porque 'rodas' é um atributo de classe, compartilhado por todos os objetos criados.

#3. O método __init__ serve para inicializar o objeto, ou seja, definir os valores iniciais dos atributos quando o objeto é criado. Se ele não for usado, o objeto é criado, mas sem atributos iniciais definidos.

#4. O código mostra ['Ana'], porque o atributo 'alunos' é compartilhado entre todas as instâncias.
#Correção:
class Sala:
    def __init__(self):
        self.alunos = []

    def adicionar(self, nome):
        self.alunos.append(nome)      
a = Sala()
b = Sala()
a.adicionar("Ana")
print(b.alunos)

#5. Usamos @property para controlar o acesso a um atributo (encapsulamento), sem precisar chamar o método com parênteses. Vantagem: permite validar ou modificar o valor ao acessar o atributo, mantendo uma interface simples.

#6. 
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura
    @property
    def perimetro(self):
        return 2 * (self.largura + self.altura)

#7. Método de instância usa 'self' e age sobre um objeto específico. Método de classe usa 'cls' e age sobre a classe toda.
#Exemplo:

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def criar_anonimo(cls):
        return cls('Anônimo')

#8. Faltava o if valor > 0 para validar o depósito.

class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

#9.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá, eu sou {self.nome}'

#10. A POO facilita a manutenção porque o código fica organizado em partes independentes (classes). Assim, é possível reaproveitar código, fazer alterações com menos impacto e entender melhor o sistema.
