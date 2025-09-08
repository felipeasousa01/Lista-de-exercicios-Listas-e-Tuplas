# Sistema de Locadora de Filmes Online 

# Lista de filmes disponíveis
filmes = [
    {"id": 1, "titulo": "Vingadores: Ultimato", "disponivel": True},
    {"id": 2, "titulo": "Harry Potter e a Pedra Filosofal", "disponivel": True},
    {"id": 3, "titulo": "O Senhor dos Anéis: A Sociedade do Anel", "disponivel": True},
    {"id": 4, "titulo": "Matrix", "disponivel": True},
    {"id": 5, "titulo": "Titanic", "disponivel": True}
]

# Lista de locações
locacoes = []

# Loop principal do sistema
while True:
    print("\n🎬 LOCADORA DE FILMES ONLINE 🎬")
    print("1 - Listar filmes")
    print("2 - Locar filme")
    print("3 - Devolver filme")
    print("4 - Encerrar sistema")
    opcao = input("Escolha uma opção: ")

    # Listar filmes
    if opcao == "1":
        print("\n📽️ Lista de Filmes:")
        for filme in filmes:
            if filme["disponivel"]:
                status = "Disponível"
            else:
                status = "Indisponível"
            print(f"{filme['id']} - {filme['titulo']} ({status})")

    # Locar filme
    elif opcao == "2":
        print("\n📽️ Lista de Filmes para locação:")
        for filme in filmes:
            status = "Disponível" if filme["disponivel"] else "Indisponível"
            print(f"{filme['id']} - {filme['titulo']} ({status})")

        escolha = int(input("\nDigite o ID do filme que deseja locar: "))
        encontrado = False
        for filme in filmes:
            if filme["id"] == escolha:
                encontrado = True
                if filme["disponivel"]:
                    filme["disponivel"] = False
                    dias = int(input("Por quantos dias deseja alugar? "))
                    locacoes.append({"id_filme": filme["id"], "dias": dias})
                    print(f"✅ Você locou '{filme['titulo']}' por {dias} dias.")
                else:
                    print("⚠️ Filme indisponível no momento.")
        if not encontrado:
            print("⚠️ Filme não encontrado.")

    # Devolver filme
    elif opcao == "3":
        if len(locacoes) == 0:
            print("\n⚠️ Nenhum filme locado no momento.")
        else:
            print("\nFilmes locados:")
            for loc in locacoes:
                for filme in filmes:
                    if filme["id"] == loc["id_filme"]:
                        print(f"{filme['id']} - {filme['titulo']} (Dias alugados: {loc['dias']})")

            escolha = int(input("\nDigite o ID do filme que deseja devolver: "))
            devolvido = False
            for loc in locacoes:
                if loc["id_filme"] == escolha:
                    for filme in filmes:
                        if filme["id"] == escolha:
                            filme["disponivel"] = True
                            atraso = int(input("Quantos dias de atraso na devolução? "))
                            if atraso > 0:
                                multa = atraso * 2.50
                                print(f"⚠️ Devolução com {atraso} dias de atraso. Multa: R${multa:.2f}")
                            else:
                                print("✅ Filme devolvido sem atraso.")
                            locacoes.remove(loc)
                            devolvido = True
                            break
            if not devolvido:
                print("⚠️ Filme não encontrado na lista de locações.")

    # Encerrar sistema
    elif opcao == "4":
        print("👋 Sistema encerrado. Obrigado por usar a Locadora Online!")
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.")
