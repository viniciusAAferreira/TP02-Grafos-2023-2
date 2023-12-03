import networkx as nx
from networkx.algorithms.cycles import find_cycle

### PRIMEIRA PARTE DO TRABALHO ###

def calcular_ordem_do_grafo_graphml(grafo):
    return grafo.number_of_nodes()

def calcular_tamanho_do_grafo(grafo):
    return grafo.number_of_edges()

def encontrar_vizinhos_do_vertice(grafo, vertice):
    vizinhos = list(grafo.neighbors(vertice))
    return vizinhos

def determinar_grau_do_vertice(grafo, vertice):
    grau = grafo.degree(vertice)
    return grau

def calcular_sequencia_de_graus(grafo):
    sequencia_de_graus = list(grafo.degree())
    return sequencia_de_graus

def determinar_excentricidade_do_vertice(grafo, vertice):
    excentricidades = nx.single_source_shortest_path_length(grafo, source=vertice)
    excentricidade = max(excentricidades.values())
    return excentricidade

def determinar_raio_do_grafo(grafo):
    raio = nx.radius(grafo)
    return raio

def determinar_diametro_do_grafo(grafo):
    diametro_do_grafo = nx.diameter(grafo)
    return diametro_do_grafo

def determinar_centro_do_grafo(grafo):
    centro_do_grafo = nx.center(grafo)
    return centro_do_grafo


def busca_em_largura_com_arvore(grafo, vertice_inicial):
    arvore_busca = nx.Graph()
    fila = [vertice_inicial]
    visitados = set(fila)
    sequencia_vertices = []  
    while fila:
        vertice_atual = fila.pop(0)
        sequencia_vertices.append(vertice_atual)

        for vizinho in grafo.neighbors(vertice_atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                arvore_busca.add_edge(vertice_atual, vizinho)

    # Arestas que não fazem parte da árvore de busca em largura
    arestas_nao_arvore = list(set(grafo.edges()) - set(arvore_busca.edges()))

    return arvore_busca, arestas_nao_arvore, sequencia_vertices

def determinar_distancia_entre_dois_vertices(grafo, vertice_origem, vertice_destino):
    distancia = nx.shortest_path_length(grafo, source=vertice_origem, target=vertice_destino, weight='weight')
    
    caminho_minimo = nx.shortest_path(grafo, source=vertice_origem, target=vertice_destino, weight='weight')

    return distancia, caminho_minimo

def calcular_centralidade_de_proximidade(grafo, vertice):
    distancias = nx.single_source_shortest_path_length(grafo, vertice)
    soma_distancias = sum(distancias.values())
    numero_de_vertices = grafo.number_of_nodes()
    centralidade_de_proximidade = (numero_de_vertices - 1) / soma_distancias
    return centralidade_de_proximidade

### SEGUNDA PARTE DO TRABALHO ###
def possui_Ciclo(grafo):
        try:
            ciclo = find_cycle(grafo, orientation='ignore')
            return True
        except nx.NetworkXNoCycle:
            return False
        
def encontrar_menor_ciclo(graph):
    menor_ciclo = None
    menor_soma_pesos = float('inf')

    for node in graph.nodes():
        # Aplica o algoritmo de busca em largura (BFS) para encontrar ciclos a partir de cada nó
        for ciclo in nx.cycle_basis(graph, node):
            soma_pesos = sum(graph[u][v]['weight'] for u, v in zip(ciclo, ciclo[1:] + [ciclo[0]]))
            if soma_pesos < menor_soma_pesos:
                menor_soma_pesos = soma_pesos
                menor_ciclo = ciclo

    return menor_ciclo, menor_soma_pesos

def gerar_arvore_geradora_minima(graph):
    mst = nx.minimum_spanning_tree(graph)

    total_weight = sum((graph[u][v]['weight'] for u, v in mst.edges()))

    return mst, total_weight

def conjunto_estavel_heuristica(graph):
    stable_set = set()

    # Ordena os vértices por grau não decrescente
    nodes_by_degree = sorted(graph.nodes(), key=lambda x: graph.degree(x))

    # Itera sobre os vértices
    for node in nodes_by_degree:
        # Adiciona o vértice ao conjunto estável se não for adjacente a nenhum vértice já presente
        if all(neighbor not in stable_set for neighbor in graph.neighbors(node)):
            stable_set.add(node)

    return stable_set

def emparelhamento_Maximo(grafo):
    matching = nx.max_weight_matching(grafo)

    return matching