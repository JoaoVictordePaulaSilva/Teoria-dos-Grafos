from GrafoMatriz import carregar_grafo, salvar_grafo, Grafo

grafo = None
nomes = []

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
