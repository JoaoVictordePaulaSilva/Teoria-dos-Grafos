from GrafoMatriz import carregar_grafo, Grafo

def ler_dados_arquivo():
    global grafo, nomes
    grafo, nomes = carregar_grafo("Grafo Teste.txt")
    print("Dados carregados com sucesso!")

def mostrar_grafo():
    if grafo:
        grafo.show()
    else:
        print("Nenhum grafo carregado ainda.")

def inserir_aresta():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return
    v = int(input("Digite o vértice de origem: "))
    w = int(input("Digite o vértice de destino: "))
    grafo.insere_aresta(v, w)
    print("Aresta inserida com sucesso!")

def remover_aresta():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return
    v = int(input("Digite o vértice de origem: "))
    w = int(input("Digite o vértice de destino: "))
    grafo.remove_aresta(v, w)
    print("Aresta removida com sucesso!")

def menu():
    global grafo, nomes
    grafo, nomes = None, None
    while True:
        print("\nMenu de opções:")
        print("a) Ler dados do arquivo grafo.txt")
        print("d) Inserir aresta")
        print("f) Remover aresta")
        print("h) Mostrar grafo")
        print("j) Encerrar a aplicação")

        escolha = input("Escolha uma opção: ").strip().lower()

        if escolha == 'a':
            ler_dados_arquivo()
        elif escolha == 'd':
            inserir_aresta()
        elif escolha == 'f':
            remover_aresta()
        elif escolha == 'h':
            mostrar_grafo()
        elif escolha == 'j':
            print("Encerrando aplicação...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
