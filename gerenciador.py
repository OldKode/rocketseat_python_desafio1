import funcoes

agenda = []
while True:
    print("\nAgenda de contatos!")
    print("\nSelecione uma das opções a seguir")
    print("1 - Adicionar contato")
    print("2 - Visualizar lista de contatos")
    print("3 - Editar contato")
    print("4 - Marcar/desmarcar como favorito")
    print("5 - Ver lista de contatos favoritos")
    print("6 - Apagar contato")

    escolha = input("Opção:")

    if escolha == "1":
        nome = input("Insira um nome:")
        telefone = input("Insira um telefone:")
        email = input("Insira um email:")

        favorito = ""
        while favorito.upper() != "S" and favorito.upper() != "N":
            favorito = input("É favorito? [S/N]")

            if favorito.upper() != "S" and favorito.upper() != "N":
                print("Opção invalida, favor informar: S ou N")
        
        if favorito.upper() == "S":
            favorito = True
        else:
            favorito = False
        
        cadastro = funcoes.gera_contato(nome, telefone, email, favorito)

        funcoes.adicionar_contato(agenda, cadastro)

    elif escolha == "2":
        funcoes.visualizar_contatos(agenda)

    elif escolha == "3":
        print("\nQual contato deseja alterar?")
        funcoes.visualizar_contatos(agenda)

        try:
            indice = int(input("Digite o Indice do contato a ser alterado:"))

        except Exception as e:
            print(f"Erro: {e}")        

        if indice >= 1 and indice  < len(agenda) + 1:
            nome = input("Insira um nome:")
            telefone = input("Insira um telefone:")
            email = input("Insira um email:") 

            favorito = ""
            while favorito.upper() != "S" and favorito.upper() != "N":
                favorito = input("É favorito? [S/N]")

                if favorito.upper() != "S" and favorito.upper() != "N":
                    print("Opção invalida, favor informar: S ou N")
            
            if favorito.upper() == "S":
                favorito = True
            else:
                favorito = False
            
            cadastro = funcoes.gera_contato(nome, telefone, email, favorito)

            funcoes.alterar_contato(agenda, indice - 1, cadastro)

            
        else:
            print("Numero de indice invalido.")

    elif escolha == "4":
        print("\nQual contato deseja alterar o favorito?")
        funcoes.visualizar_contatos(agenda)

        try:
            indice = int(input("Digite o Indice:"))

        except Exception as e:
            print(f"Erro: {e}")

        if indice >= 1 and indice  < len(agenda) + 1:
            funcoes.favoritar(agenda, indice - 1)
        else:
            print("Numero de indice invalido.")

    elif escolha == "5":
        funcoes.listar_favoritos(agenda)

    elif escolha == "6":
        print("\nQual contato deseja remnover?")
        funcoes.visualizar_contatos(agenda)

        try:
            indice = int(input("Digite o Indice:"))

        except Exception as e:
            print(f"Erro: {e}")

        if indice >= 1 and indice  < len(agenda) + 1:
            funcoes.apagar_contato(agenda, indice - 1)
        else:
            print("Numero de indice invalido.")