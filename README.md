# Relatório do Projeto: Sistema de Localização Cajo Traffic System com Dijkstra
YT: https://www.youtube.com/watch?v=uD7tosCv0hA&ab_channel=TrabalhosMackCien1
## 1. Introdução

O presente relatório documenta o desenvolvimento do **Cajo Traffic System**, um sistema de manipulação de grafos voltado para aplicações de localização urbana. O sistema permite carregar, salvar e manipular grafos representados por matrizes de adjacência, simulando a estrutura de uma malha urbana.

Como aprimoramento, foi incorporado o **algoritmo de Dijkstra** para o cálculo do **caminho mínimo entre vértices**, permitindo simular rotas otimizadas em redes urbanas, como deslocamentos por vias públicas.

A aplicação está dividida em três módulos principais:

- `GrafoMatriz.py`: implementação da estrutura de dados do grafo.
- `GrafoTeste.py`: operações e funções de entrada/saída para manipulação do grafo.
- `main.py`: interface de menu interativo com o usuário.

## 2. Objetivos

- Implementar uma estrutura de grafo orientado utilizando matriz de adjacência.
- Permitir operações como inserção e remoção de vértices e arestas.
- Permitir o carregamento e salvamento de dados em arquivos `.txt`.
- Determinar propriedades do grafo como grau, simetria e conexidade.
- **Implementar o algoritmo de Dijkstra** para cálculo do menor caminho entre dois pontos.

## 3. Estrutura dos Arquivos

### 3.1 `GrafoMatriz.py`

Contém a classe `Grafo`, que representa um grafo direcionado com as seguintes funcionalidades:

- Inserção e remoção de vértices e arestas.
- Impressão da matriz de adjacência.
- Cálculo de grau de entrada, grau de saída, e grau total.
- Verificação de simetria.
- Identificação de fontes e sorvedouros.
- Verificação de conexidade (a partir do vértice 0).
- **Algoritmo de Dijkstra** para menor caminho entre dois vértices.
- **Algoritmo de Bellman-Ford** para calcular o menor caminho.
- **Algoritmo de Floyd** para calcular menor caminho.

Funções adicionais:

- `carregar_grafo(arquivo)`: carrega um grafo de um arquivo `.txt`.
- `salvar_grafo(arquivo, grafo, nomes_vertices)`: salva o grafo em arquivo `.txt`.

### 3.2 `GrafoTeste.py`

Implementa funcionalidades para interação com o grafo:

- Leitura e gravação de dados.
- Inserção/remoção de vértices e arestas.
- Impressão do conteúdo do arquivo.
- Impressão da matriz do grafo.
- Apresentação da conexidade.
- **Execução do Dijkstra** com seleção de vértices de origem e destino.

### 3.3 `main.py`

Arquivo principal da aplicação com um menu interativo que permite ao usuário:

- Ler e gravar dados em `grafo.txt`.
- Inserir/remover vértices e arestas.
- Visualizar o grafo e seu estado no arquivo.
- Verificar conexidade e apresentar forma reduzida.
- **Executar o algoritmo de Dijkstra** para rotas mais curtas.
- Encerrar a aplicação.

## 4. Funcionamento Geral do Sistema

O sistema opera por meio de um menu textual com opções como:

- **a)** Ler dados de `grafo.txt`
- **b)** Gravar dados em `grafo.txt`
- **c)** Inserir vértice
- **d)** Inserir aresta
- **e)** Remover vértice
- **f)** Remover aresta
- **g)** Mostrar conteúdo do arquivo
- **h)** Mostrar grafo
- **i)** Verificar conexidade
- **j)** Calcular menor caminho com Dijkstra
- **k)** Calcular menor caminho com Bellman-Ford
- **k)** Calcular menor caminho com Floyd
- **m)** Encerrar aplicação

As funcionalidades interagem com o grafo em memória e com o arquivo `grafo.txt`, permitindo edições persistentes e análises dinâmicas.

## 🧪 5. Testes Recomendados

- Testar inserção e remoção de vértices e arestas.
- Verificar leitura e gravação com diferentes grafos.
- Avaliar conexidade em grafos com componentes isolados.
- Testar simetria em grafos direcionados e não direcionados.
- **Testar o algoritmo de Dijkstra com diferentes pares de vértices.**

## 🌍 6. Relação com os Objetivos de Desenvolvimento Sustentável (ODS)

Este projeto se relaciona com os seguintes ODS:

### 🎯 ODS 11: Cidades e Comunidades Sustentáveis

> O algoritmo de Dijkstra possibilita a **simulação de rotas mais eficientes**, contribuindo para a redução do trânsito urbano, otimização de deslocamentos e emissão de poluentes — fatores fundamentais para tornar as cidades mais sustentáveis e inteligentes.

### 🎯 ODS 9: Indústria, Inovação e Infraestrutura

> A manipulação de grafos e rotas com algoritmos como Dijkstra contribui para o **planejamento inteligente de infraestrutura urbana**, otimizando o uso de vias e reduzindo gargalos logísticos em sistemas de transporte.

## 🏁 7. Conclusão

O **Cajo Traffic System** apresenta uma solução educacional e prática para manipulação de grafos voltados a sistemas urbanos. Com a adição do **algoritmo de Dijkstra**, torna-se possível simular caminhos mínimos em mapas urbanos, aumentando o valor da aplicação para fins como roteamento, logística e mobilidade urbana sustentável.
