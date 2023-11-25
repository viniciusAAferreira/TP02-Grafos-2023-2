import networkx as nx
from funcoes import *
import matplotlib.pyplot as plt

# arquivo_graphml = "./Arquivos/exemplo_BuscaLargura_Slide.graphml"

# grafo = nx.read_graphml(arquivo_graphml)
# opcao = -1

# pos = nx.planar_layout(grafo)

arq = "./Arquivos/"
arquivo = input("Digite o nome do arquivo do grafo: ")
arquivo_graphml = arq + arquivo + '.graphml'

try:
    grafo = nx.read_graphml(arquivo_graphml)
    opcao = -1

    # Cria um layout para o grafo
    pos = nx.planar_layout(grafo)

except (IOError, FileNotFoundError) as e:
    print(f"Erro na leitura do arquivo: {e}")

nx.draw(grafo, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold')
edge_labels = nx.get_edge_attributes(grafo, "weight")
nx.draw_networkx_edge_labels(grafo, pos, edge_labels)

plt.title("Grafo Lido do Arquivo GraphML")
ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()


while opcao != 0:
    print("#############################################")
    print("1 - Verificar se o grafo possui ciclo")
    print("2 - Encontrar o menor ciclo")
    print("3 - Determinar a árvore geradora mínima")
    print("4 - Determinar um conjunto estável de vértices de um grafo por meio de uma heurística")
    print("5 - Determinar o emparelhamento máximo em um grafo")
    print("0 - Sair")
    print("#############################################")
    

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        tem_Ciclo = possui_Ciclo(grafo)
        if tem_Ciclo:
            print("Grafo possui ciclo")
        else:
            print("Grafo não possui ciclo")
        print("\n")

    elif opcao == 2:
        print("\n")

    elif opcao == 3:
        print("\n")

    elif opcao == 4:
        print("\n")
    
    elif opcao == 5:
        print("\n")
    
    elif opcao == 0:
        print("\n")
        print("Saindo do programa...")

    else:
        print("Opção inválida. Por favor, tente novamente.")
        print("\n")