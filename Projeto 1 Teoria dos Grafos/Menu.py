def menu():
    while True:
        print("\nMenu de opções:")
        print("a) Ler dados do arquivo grafo.txt")
        print("b) Gravar dados no arquivo grafo.txt")
        print("c) Inserir vértice")
        print("d) Inserir aresta")
        print("e) Remover vértice")
        print("f) Remover aresta")
        print("g) Mostrar conteúdo do arquivo")
        print("h) Mostrar grafo")
        print("i) Apresentar a conexidade do grafo e o reduzido")
        print("j) Encerrar a aplicação")

        escolha = input("Escolha uma opção: ")

        if escolha == 'a':
            ler_dados_arquivo()
        elif escolha == 'b':
            gravar_dados_arquivo()
        elif escolha == 'c':
            inserir_vertice()
        elif escolha == 'd':
            inserir_aresta()
        elif escolha == 'e':
            remover_vertice()
        elif escolha == 'f':
            remover_aresta()
        elif escolha == 'g':
            mostrar_conteudo_arquivo()
        elif escolha == 'h':
            mostrar_grafo()
        elif escolha == 'i':
            apresentar_conexidade()
        elif escolha == 'j':
            encerrar_aplicacao()
        else:
            print("Opção inválida. Tente novamente.")

menu()