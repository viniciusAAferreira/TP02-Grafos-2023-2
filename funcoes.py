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