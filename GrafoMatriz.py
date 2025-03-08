class TGrafo:
    def __init__(self, n):
        self.n = n  # Quantidade de vértices
        self.m = 0  # Quantidade de arestas
        self.adj = [[0] * n for _ in range(n)]  # Matriz de adjacência inicializada com zeros
    
    def insereA(self, v, w):
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.m += 1
    
    def removeA(self, v, w):
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.m -= 1
    
    def show(self):
        print(f"n: {self.n}")
        print(f"m: {self.m}")
        for i in range(self.n):
            print()
            for w in range(self.n):
                print(f"Adj[{i},{w}]= {self.adj[i][w]}", end=" ")
        print("\n\nfim da impressao do grafo.")
    
    def in_degree(self, v):
        return sum(self.adj[w][v] for w in range(self.n))
    
    def out_degree(self, v):
        return sum(self.adj[v][w] for w in range(self.n))
    
    def degree(self, v):
        return self.in_degree(v) + self.out_degree(v)
    
    def fonte(self, v):
        return 1 if self.in_degree(v) == 0 and self.out_degree(v) > 0 else 0
    
    def sorvedouro(self, v):
        return 1 if self.in_degree(v) > 0 and self.out_degree(v) == 0 else 0
    
    def simetria(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] != self.adj[j][i]:
                    return 0
        return 1

# Função para mapear cidades a índices
def cidade_para_indice(cidade, cidades_dict):
    if cidade not in cidades_dict:
        cidades_dict[cidade] = len(cidades_dict)
    return cidades_dict[cidade]


# Função principal para ler o arquivo e criar o grafo
def criar_grafo_com_arquivo(nome_arquivo):
    grafo = {}
    arestas = []

    with open(nome_arquivo, 'r', encoding='utf-8-sig') as file:  # Usando encoding='utf-8-sig' para ignorar o BOM
        linhas = file.readlines()

        # Lê o número de vértices
        num_vertices = int(linhas[0].strip())  # Agora a linha não terá o BOM

        # Lê os vértices
        for i in range(1, num_vertices + 1):
            linha = linhas[i].strip()
            if linha:  # Verifica se a linha não está vazia
                partes = linha.split()
                if len(partes) >= 2:  # Verifica se há pelo menos 2 elementos
                    vertice = partes[1]
                    grafo[vertice] = []  # Cria a chave para cada vértice

        # Lê o número de arestas
        num_arestas = int(linhas[num_vertices + 1].strip())

        # Lê as arestas
        for i in range(num_vertices + 2, len(linhas)):
            linha = linhas[i].strip()
            if linha:  # Verifica se a linha não está vazia
                partes = linha.split()
                if len(partes) == 2:  # Verifica se há exatamente 2 elementos
                    aresta = (partes[0], partes[1])
                    arestas.append(aresta)

                    # Verifica se os vértices estão no grafo, e se não estiverem, os cria
                    if aresta[0] not in grafo:
                        grafo[aresta[0]] = []
                    if aresta[1] not in grafo:
                        grafo[aresta[1]] = []

                    # Adiciona a aresta ao grafo
                    grafo[aresta[0]].append(aresta[1])
                    grafo[aresta[1]].append(aresta[0])

    return grafo

nome_arquivo = 'Grafo Teste.txt'
grafo = criar_grafo_com_arquivo(nome_arquivo)
print(grafo)
