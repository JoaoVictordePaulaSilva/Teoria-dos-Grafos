class Grafo:
    def __init__(self, n):
        self.n = n  # Número de vértices
        self.m = 0  # Número de arestas
        self.adj = [[0] * n for _ in range(n)]  # Matriz de adjacência

    def insere_aresta(self, v, w):
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.m += 1

    def remove_aresta(self, v, w):
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.m -= 1

    def show(self):
        print(f"n: {self.n}")
        print(f"m: {self.m}")
        for i in range(self.n):
            print(" ".join(map(str, self.adj[i])))
        print("\nFim da impressão do grafo.")

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


def carregar_grafo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    num_vertices = int(linhas[1].strip())
    grafo = Grafo(num_vertices)
    
    nomes_vertices = {}
    for i in range(2, 2 + num_vertices):
        partes = linhas[i].strip().split(" ", 1)
        nomes_vertices[int(partes[0])] = partes[1].strip('"')
    
    num_arestas = int(linhas[2 + num_vertices].strip())
    for i in range(3 + num_vertices, 3 + num_vertices + num_arestas):
        v, w = map(int, linhas[i].strip().split())
        grafo.insere_aresta(v, w)
    
    return grafo, nomes_vertices

# Uso
grafo, nomes = carregar_grafo("Grafo Teste.txt")
grafo.show()