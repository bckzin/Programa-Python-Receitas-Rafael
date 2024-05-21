import ADD, VISU, ATUA, DEL, ALEA, COM 

while True:

        file = open("BancoDados.txt","a")
        cadastros = {}

        while True:
            print("---------------------------------")
            print("----GERENCIAMENTO DE RECEITAS----")
            print("---------------------------------")
            print("---------MENU DE OPÇÕES----------")
            print("\n[1] - ADICIONAR RECEITAS")
            print("[2] - VISUALIZAR RECEITAS")
            print("[3] - ATUALIZAR RECEITAS")
            print("[4] - DELETAR RECEITAS")
            print("[5] - SALVAR RECEITAS")
            print("[6] - RECEITA ALEATÓRIA")
            print("[7] - COMENTÁRIOS")
            print("[8] - SAIR")
            try: 
                while True:
                    escolha = int(input("Opção desejada : "))
                    if 1 <= escolha <= 8:
                        break

            except ValueError:
                print("Digite um número.")

            if escolha == 1:  #Opção para adicionar uma receita
                cadastros = ADD.adicionar(cadastros)

            elif escolha == 2:  #Opção para visualizar receitas
                VISU.visualizar(cadastros)

            elif escolha == 3:  #Opção para atualizar uma receita
                cadastros = ATUA.atualizar(cadastros)

            elif escolha == 4:  #Opção para deletar uma receita
                cadastros = DEL.deletar(cadastros)

            elif escolha == 5:  #Opção para salvar a(s) receitas
                file=open("BancoDados.txt","a")
                file.write(str(f"{cadastros}\n"))
                print("Receitas salvas!")

            elif escolha == 6:  #Opção para receita aleatória
                ALEA.aleatoria(cadastros)

            elif escolha == 7:  #Opção para adicionar comentário
                COM.comentario(cadastros)

            elif escolha == 8:  #Opção sair do programa
                file.close()
                exit()
