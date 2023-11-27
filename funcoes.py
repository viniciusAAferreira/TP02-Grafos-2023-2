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
    min_cycle = None
    min_cycle_weight = float('inf')

    for start_node in graph.nodes():
        visited = set()
        stack = [(start_node, [start_node], 0)]

        while stack:
            current_node, path, path_weight = stack.pop()

            for neighbor, weight in graph[current_node].items():
                if neighbor not in path:
                    new_path = path + [neighbor]
                    new_weight = path_weight + weight['weight']

                    if new_weight < min_cycle_weight:
                        stack.append((neighbor, new_path, new_weight))

                    # Verifica se o caminho forma um ciclo menor
                    if new_weight < min_cycle_weight and neighbor == start_node:
                        min_cycle = new_path
                        min_cycle_weight = new_weight

    return min_cycle, min_cycle_weight