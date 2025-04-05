from GrafoTeste import (
    ler_dados_arquivo, gravar_dados_arquivo, inserir_vertice, 
    inserir_aresta, remover_vertice, remover_aresta, 
    mostrar_conteudo_arquivo, mostrar_grafo, apresentar_conexidade
)
def menu():
    global grafo, nomes
    grafo, nomes = None, None
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

        escolha = input("Escolha uma opção: ").strip().lower()

        if escolha == 'a' or escolha == 'A':
            ler_dados_arquivo()
        elif escolha == 'b' or escolha == 'B':
            gravar_dados_arquivo()
        elif escolha == 'c' or escolha == 'C':
            inserir_vertice()
        elif escolha == 'd' or escolha == 'D':
            inserir_aresta()
        elif escolha == 'e' or escolha == 'E':
            remover_vertice()
        elif escolha == 'f' or escolha == 'F':  
            remover_aresta()
        elif escolha == 'g' or escolha == 'G':
            mostrar_conteudo_arquivo()
        elif escolha == 'h' or escolha == 'H':
            mostrar_grafo()
        elif escolha == 'i' or escolha == 'I':
            apresentar_conexidade()
        elif escolha == 'j' or escolha == 'J':
            print("Encerrando aplicação...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
