# Neste primeiro projeto, utilizaremos os conhecimentos de listas, for e while, condicionais, para desenvolver uma locadora DE FILMES ONLINE com 4 funções (listagem, locação, devolução e encerramento do sistema).Multa por atraso. 

# Sistema de Locadora de Filmes Online

# Lista de filmes e séries disponíveis para locação
filmes = [
    {"id": 1, "titulo": "Vingadores: Ultimato", "disponivel": True},
    {"id": 2, "titulo": "Harry Potter e a Pedra Filosofal", "disponivel": True},
    {"id": 3, "titulo": "O Senhor dos Anéis: A Sociedade do Anel", "disponivel": True},
    {"id": 4, "titulo": "Matrix", "disponivel": True},
    {"id": 5, "titulo": "Titanic", "disponivel": True}
]
    
# Lista de locações ativas
locacoes = []

# Função para listar os filmes
def listar_filmes():
    print("\n📽️ Lista de Filmes:")
    for filme in filmes:
        status = "Disponível" if filme["disponivel"] else "Indisponível"
        print(f"{filme['id']} - {filme['titulo']} ({status})")

# Função para locar filme
def locar_filme():
    listar_filmes()
    escolha = int(input("\nDigite o ID do filme que deseja locar: "))
    for filme in filmes:
        if filme["id"] == escolha:
            if filme["disponivel"]:
                filme["disponivel"] = False
                dias = int(input("Por quantos dias deseja alugar? "))
                locacoes.append({"id_filme": filme["id"], "dias": dias})
                print(f"✅ Você locou '{filme['titulo']}' por {dias} dias.")
            else:
                print("⚠️ Filme indisponível no momento.")
            return
    print("⚠️ Filme não encontrado.")

# Função para devolver filme com cálculo de multa
def devolver_filme():
    if not locacoes:
        print("\n⚠️ Nenhum filme locado no momento.")
        return
    
    print("\nFilmes locados:")
    for loc in locacoes:
        for filme in filmes:
            if filme["id"] == loc["id_filme"]:
                print(f"{filme['id']} - {filme['titulo']} (Dias alugados: {loc['dias']})")
    
    escolha = int(input("\nDigite o ID do filme que deseja devolver: "))
    for loc in locacoes:
        if loc["id_filme"] == escolha:
            for filme in filmes:
                if filme["id"] == escolha:
                    filme["disponivel"] = True
                    atraso = int(input("Quantos dias de atraso na devolução? "))
                    if atraso > 0:
                        multa = atraso * 2.50  # multa de R$2,50 por dia de atraso
                        print(f"⚠️ Filme devolvido com {atraso} dias de atraso. Multa: R${multa:.2f}")
                    else:
                        print("✅ Filme devolvido sem atraso.")
                    locacoes.remove(loc)
                    return
    print("⚠️ Filme não encontrado na lista de locações.")

# Função principal
def menu():
    while True:
        print("\n🎬 LOCADORA DE FILMES ONLINE 🎬")
        print("1 - Listar filmes")
        print("2 - Locar filme")
        print("3 - Devolver filme")
        print("4 - Encerrar sistema")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_filmes()
        elif opcao == "2":
            locar_filme()
        elif opcao == "3":
            devolver_filme()
        elif opcao == "4":
            print("👋 Sistema encerrado. Obrigado por usar a Locadora Online!")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")