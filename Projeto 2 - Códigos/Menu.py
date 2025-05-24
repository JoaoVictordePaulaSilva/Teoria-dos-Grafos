from GrafoTeste import (
    ler_dados_arquivo, gravar_dados_arquivo, inserir_vertice, 
    inserir_aresta, remover_vertice, remover_aresta, 
    mostrar_conteudo_arquivo, mostrar_grafo, apresentar_conexidade, 
    apresentar_dijkstra, apresentar_bellman_ford, apresentar_floyd
)

def menu():
    while True:
        print("\nBem vindo ao Cajo Traffic System")
        print("Menu de opções:")
        print("a) Ler dados do arquivo grafo.txt")
        print("b) Gravar dados no arquivo grafo.txt")
        print("c) Inserir vértice")
        print("d) Inserir aresta")
        print("e) Remover vértice")
        print("f) Remover aresta")
        print("g) Mostrar conteúdo do arquivo")
        print("h) Mostrar grafo")
        print("i) Apresentar a conexidade do grafo")
        print("j) Apresentar o caminho com Dijkstra")
        print("k) Apresentar o caminho com Bellman-Ford")
        print("l) Apresentar o caminho com Floyd")
        print("m) Encerrar a aplicação")

        escolha = input("Escolha uma opção: ").strip().lower()

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
            apresentar_dijkstra()
        elif escolha == 'k':
            apresentar_bellman_ford()
        elif escolha == 'l':
            apresentar_floyd()
        elif escolha == 'm':
            print("Encerrando aplicação...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
