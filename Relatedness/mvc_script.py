#!/usr/bin/env python3

import pandas as pd
import networkx as nx

def minimize_edges_keep_nodes(csv_filepath):
    """
    Minimalizuje počet hran v grafu příbuzenských vztahů pomocí aproximace Minimum Vertex Cover.

    Args:
        csv_filepath: Cesta k CSV souboru s dvojicemi příbuzných vlků.

    Returns:
        tuple: (množina zachovaných uzlů (vlků), upravený graf). Vrátí (None, None) v případě chyby.
    """
    try:
        df = pd.read_csv(csv_filepath, header=None, names=['wolf1', 'wolf2'])
        graph = nx.Graph()
        graph.add_edges_from(zip(df['wolf1'], df['wolf2']))

        # Aproximace Minimum Vertex Cover (greedy algoritmus)
        vertex_cover = set()
        edges = list(graph.edges())
        while edges:
            edge = edges.pop(0)
            if edge[0] not in vertex_cover and edge[1] not in vertex_cover:
                vertex_cover.add(edge[0])
                
        #zachováváme jen to co není ve vertex cover
        remaining_nodes = set(graph.nodes()) - vertex_cover
        
        #Vytvoříme nový graf s zachovanými uzly
        new_graph = graph.subgraph(remaining_nodes)

        return remaining_nodes, new_graph

    except FileNotFoundError:
        print(f"Soubor '{csv_filepath}' nenalezen.")
        return None, None
    except Exception as e:
        print(f"Chyba: {e}")
        return None, None

# Příklad použití:
csv_file = "wolf_relationships.csv" #Vložte název svého CSV souboru
remaining_nodes, new_graph = minimize_edges_keep_nodes(csv_file)


if remaining_nodes is not None:
    print("Zachované uzly (vlci):", remaining_nodes)
    print("\nUpravený graf (hrany):", new_graph.edges())
