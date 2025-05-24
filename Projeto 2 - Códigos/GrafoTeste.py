from GrafoMatriz import carregar_grafo, salvar_grafo, Grafo

grafo = None
nomes = {}

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

    if v >= grafo.n or w >= grafo.n or v < 0 or w < 0:
        print("Vértice(s) inválido(s).")
        return

    grafo.insere_aresta(v, w)
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
        with open("grafo.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            if not conteudo.strip():
                print("O arquivo está vazio.")
            else:
                print("Conteúdo do arquivo grafo.txt:")
                print(conteudo)
    except FileNotFoundError:
        print("Arquivo grafo.txt não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")


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

def apresentar_dijkstra():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return
    print("Vértices disponíveis:")
    for v in nomes:
        print(f"{v}: {nomes[v]}")
    try:
        origem = int(input("Digite o número do vértice de origem: "))
        destino = int(input("Digite o número do vértice de destino: "))
        if origem >= grafo.n or destino >= grafo.n:
            print("Índice de vértice inválido.")
            return
        distancia, caminho = grafo.dijkstra(origem, destino)
        if distancia == float("inf"):
            print("Não existe caminho entre os vértices fornecidos.")
        else:
            nomes_caminho = [nomes.get(v, f"V{v}") for v in caminho]
            print(f"Caminho mais curto de {nomes[origem]} para {nomes[destino]}:")
            print(" -> ".join(nomes_caminho))
            print(f"Distância total: {distancia}")
    except ValueError:
        print("Entrada inválida.")

def apresentar_bellman_ford():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return
    print("Vértices disponíveis:")
    for v in nomes:
        print(f"{v}: {nomes[v]}")
    try:
        origem = int(input("Digite o número do vértice de origem: "))
        destino = int(input("Digite o número do vértice de destino: "))
        if origem >= grafo.n or destino >= grafo.n:
            print("Índice de vértice inválido.")
            return
        distancia, caminho = grafo.bellman_ford(origem, destino)
        if distancia == float("inf"):
            print("Não existe caminho entre os vértices fornecidos.")
        elif not caminho:
            print("Erro: ciclo de peso negativo detectado.")
        else:
            nomes_caminho = [nomes.get(v, f"V{v}") for v in caminho]
            print(f"Caminho mais curto de {nomes[origem]} para {nomes[destino]}:")
            print(" -> ".join(nomes_caminho))
            print(f"Distância total: {distancia}")
    except ValueError:
        print("Entrada inválida.")


def apresentar_floyd():
    if not grafo:
        print("Nenhum grafo carregado ainda.")
        return

    print("Executando algoritmo de Floyd-Warshall...")

    dist, prox = grafo.floyd_warshall()

    print("Vértices disponíveis:")
    for v in nomes:
        print(f"{v}: {nomes[v]}")
    try:
        origem = int(input("Digite o número do vértice de origem: "))
        destino = int(input("Digite o número do vértice de destino: "))
        if origem >= grafo.n or destino >= grafo.n:
            print("Índice de vértice inválido.")
            return

        if dist[origem][destino] == float("inf"):
            print("Não existe caminho entre os vértices fornecidos.")
            return

        # Reconstrução do caminho
        caminho = []
        atual = origem
        while atual != destino:
            if atual == -1:
                print("Não existe caminho entre os vértices fornecidos.")
                return
            caminho.append(atual)
            atual = prox[atual][destino]
        caminho.append(destino)

        nomes_caminho = [nomes.get(v, f"V{v}") for v in caminho]
        print(f"Caminho mais curto de {nomes[origem]} para {nomes[destino]}:")
        print(" -> ".join(nomes_caminho))
        print(f"Distância total: {dist[origem][destino]}")
    except ValueError:
        print("Entrada inválida.")
