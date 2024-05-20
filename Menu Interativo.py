file = open("BancoDados.txt","a")
cadastros = {}

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
