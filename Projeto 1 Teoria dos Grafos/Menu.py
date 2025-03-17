from GrafoMatriz import carregar_grafo, salvar_grafo, Grafo

def apresentar_conexidade():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return
    conexidade, grafo_reduzido = grafo.verificar_conexidade() 
    print(f"O grafo é {conexidade}.")
    if grafo_reduzido:
        print("Grafo reduzido:")
        grafo_reduzido.show()

def ler_dados_arquivo():
    global grafo, nomes
    grafo, nomes = carregar_grafo("grafo.txt")
    print("Dados carregados com sucesso!")

def gravar_dados_arquivo():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return
    salvar_grafo("grafo.txt", grafo, nomes)
    print("Dados gravados com sucesso!")

def inserir_vertice():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return
    rotulo = input("Digite o rótulo do vértice: ")
    grafo.insere_vertice(rotulo)
    print("Vértice inserido com sucesso!")

def inserir_aresta():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return
    v = int(input("Digite o vértice de origem: "))
    w = int(input("Digite o vértice de destino: "))
    peso = float(input("Digite o peso da aresta (0 se não houver peso): "))
    grafo.insere_aresta(v, w, peso)
    print("Aresta inserida com sucesso!")

def remover_vertice():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return
    v = int(input("Digite o vértice a ser removido: "))
    grafo.remove_vertice(v)
    print("Vértice removido com sucesso!")

def remover_aresta():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return
    v = int(input("Digite o vértice de origem: "))
    w = int(input("Digite o vértice de destino: "))
    grafo.remove_aresta(v, w)
    print("Aresta removida com sucesso!")

def mostrar_conteudo_arquivo():
    try:
        with open("grafo.txt", "r") as arquivo:
            print("Conteúdo do arquivo grafo.txt:")
            print(arquivo.read())
    except FileNotFoundError:
        print("Arquivo grafo.txt não encontrado.")

def mostrar_grafo():
    if grafo:
        grafo.show()
    else:
        print("Nenhum grafo carregado ainda.")

def apresentar_conexidade():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return
    conexidade, grafo_reduzido = grafo.verificar_conexidade()
    print(f"O grafo é {conexidade}.")
    if grafo_reduzido:
        print("Grafo reduzido:")
        grafo_reduzido.show()

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
            print("Encerrando aplicação...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
