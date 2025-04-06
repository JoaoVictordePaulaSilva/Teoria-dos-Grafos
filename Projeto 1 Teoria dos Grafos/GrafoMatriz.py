#Caio Teixeira Torres RA: 10417478  - Responsável pelas correções, criação do Grafo modelo e modificações no código para melhor funcionamento.
#João Victor de Paula Silva RA: 10418556 - Responsável pelo o ínicio e criação da classe grafo para o funcionamento das funções de manipular o arquivo. 
#Principais mudanças feitas - Caio Teixeira Torres: Correção do insere vértice e alguns erros de formatação no menu e funções. 
#Principais mudanças feitas - João Victor de Paula Silva: Criação e modificação conforme mudanças do projeto. 

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

    def insere_vertice(self, rotulo):
        self.n += 1
        for linha in self.adj:
            linha.append(0)
        self.adj.append([0] * self.n)

    def remove_vertice(self, v):
        if v >= self.n:
            print("Vértice inválido.")
            return
        self.n -= 1
        del self.adj[v] 
        for linha in self.adj:
            del linha[v]  

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

    def verificar_conexidade(self):
        visitado = [False] * self.n
        self.vizinhanca(0, visitado)

        if all(visitado):
            return "conexo", None
        else:
            return "desconexo", self
    def vizinhanca(self, v, visitado):
        visitado[v] = True
        for w in range(self.n):
            if self.adj[v][w] == 1 and not visitado[w]:
                self.vizinhanca(w, visitado)    

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

def salvar_grafo(arquivo, grafo, nomes_vertices):
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write("Grafo\n")
        f.write(f"{grafo.n}\n")  # Número de vértices

        # Escrevendo os nomes dos vértices
        for v in range(grafo.n):
            nome = nomes_vertices.get(v, f"V{v}")  # Usa um nome padrão caso não exista
            f.write(f'{v} "{nome}"\n')

        f.write(f"{grafo.m}\n")  # Número de arestas

        # Escrevendo as arestas
        for v in range(grafo.n):
            for w in range(grafo.n):
                if grafo.adj[v][w] == 1:
                    f.write(f"{v} {w}\n")

    print("Grafo salvo com sucesso!")
