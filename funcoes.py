import networkx as nx
from networkx.algorithms.cycles import find_cycle

def possui_Ciclo(grafo):
        try:
            # Tenta encontrar um ciclo no grafo
            ciclo = find_cycle(grafo, orientation='ignore')
            return True
        except nx.NetworkXNoCycle:
            # Se não encontrar ciclo, retorna False
            return False
        
def emparelhamento_Maximo(grafo):
    # Encontrar o emparelhamento máximo
    matching = nx.max_weight_matching(grafo)

    return matching
#1) Ordene os vértices por grau não decrescente.
#2)Inicialize um conjunto vazio para armazenar o conjunto estável.
#3) Itere sobre os vértices na ordem do passo 1. Para cada vértice:
#       Adicione o vértice ao conjunto estável se ele não for adjacente a nenhum vértice já presente no conjunto estável.
def stable_set_heuristic(graph):
    stable_set = set()

    # Ordena os vértices por grau não decrescente
    nodes_by_degree = sorted(graph.nodes(), key=lambda x: graph.degree(x))

    # Itera sobre os vértices
    for node in nodes_by_degree:
        # Adiciona o vértice ao conjunto estável se não for adjacente a nenhum vértice já presente
        if all(neighbor not in stable_set for neighbor in graph.neighbors(node)):
            stable_set.add(node)

    return stable_set

def generate_minimum_spanning_tree(graph):
    # Encontrar a árvore geradora mínima
    mst = nx.minimum_spanning_tree(graph)

    # Calcular o peso total da árvore geradora mínima
    total_weight = sum((graph[u][v]['weight'] for u, v in mst.edges()))

    return mst, total_weight

def find_minimum_cycle(graph):
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