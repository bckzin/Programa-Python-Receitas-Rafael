file = open("BancoDados.txt","a")
cadastros = {}

while True:
    print("""
    ---------------------------------
    Gerenciamento de Receitas
    ---------------------------------

    OPÇÕES:
    [1] - ADICIONAR
    [2] - VISUALIZAR
    [3] - ATUALIZAR
    [4] - DELETAR

    [5] - SALVAR
    [6] - SAIR

    """)
    escolha = int(input("Opção desejada : "))

    if escolha == 1:
        while True:
            vetor1 = []
            vetor2 = []

            receita = input("Nome da receita : ")
            pais = input("País de Origem : ").capitalize()

            qntd = int(input("\nQuantidade de ingredientes : "))
            print("-Lista de Ingredientes-")
            for i in range(qntd):
                ingredientes = (input(f"{i + 1}º Ingrediente : "))
                vetor1.append(f"{i + 1}º ingrediente = {ingredientes}")
                ing = ", ".join(vetor1)

            passos = int(input("\nQuantidade de passos do preparo : "))
            print("-Passos do Preparo-")
            for j in range(passos):
                preparo = (input(f"{j + 1}º Passo : "))
                vetor2.append(f"{i + 1}º passo = {preparo}")
                prep = ", ".join(vetor2)


            arquivo = open("receitas.txt", "a")
            arquivo.write(f"RECEITA : {receita} | ORIGEM : {pais} | INGREDIENTES : {ing} | PREPARO : {prep}\n")

            continuar = input("Deseja continuar adicionando receitas [S] ou [N] : ").upper()

            if continuar == "N":
                arquivo.close()
                arquivo = open("receitas.txt", "r")
                print(arquivo.read())
                break

            elif continuar != "S":
                print("Opção inválida, saindo...")
                break

    elif escolha == 2:
        arquivo = open("receitas.txt", "r")
        print(arquivo.read())

    elif escolha == 3:  # Opção para atualizar uma receita
        receita_atualizar = input("Nome da receita para atualizar: ")
        if receita_atualizar in cadastros:
            print(f"Receita '{receita_atualizar}' encontrada.")
            print("Atualizando informações...")
            pais = input("País de Origem (Deixe em branco para não alterar): ").capitalize()
            if pais:
                cadastros[receita_atualizar]["origem"] = pais
            qntd = int(input("Quantidade de ingredientes (Deixe 0 para não alterar): "))
            if qntd > 0:
                ingredientes = []
                print("\n-Lista de Ingredientes Atualizada-")
                for i in range(qntd):
                    ingredientes.append(input(f"{i + 1}º Ingrediente : "))
                cadastros[receita_atualizar]["ingredientes"] = ingredientes

            passos = int(input("Quantidade de passos do preparo (Deixe 0 para não alterar): "))
            if passos > 0:
                preparo = []
                print("\n-Passos do Preparo Atualizado-")
                for j in range(passos):
                    preparo.append(input(f"{j+ 1}º Passo : "))
                cadastros[receita_atualizar]["preparo"] = preparo

            print("Receita atualizada com sucesso!")
            print(cadastros)
        else:
            print(f"Receita '{receita_atualizar}' não encontrada.")

    else:
        print("Opção não cadastrada.")
