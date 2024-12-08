"""
  An algorithm that minimizes the number of edges in a kinship graph using the Minimum Vertex Cover approximation.
    Args: csv_filepath: Path to CSV file with pairs of related wolves.
    Returns: tuple: (set of kept nodes (wolves), adjusted graph). Returns (None, None) in case of error.
"""


#!/usr/bin/env python3

import pandas as pd
import networkx as nx

def minimize_edges_keep_nodes(csv_filepath):
  
    try:
        df = pd.read_csv(csv_filepath, header=None, names=['wolf1', 'wolf2'])
        graph = nx.Graph()
        graph.add_edges_from(zip(df['wolf1'], df['wolf2']))

        # approximate minimum vertex coverage (greedy algorithm)
        vertex_cover = set()
        edges = list(graph.edges())
        while edges:
            edge = edges.pop(0)
            if edge[0] not in vertex_cover and edge[1] not in vertex_cover:
                vertex_cover.add(edge[0])
                
        # kept only what is not in vertex cover
        remaining_nodes = set(graph.nodes()) - vertex_cover
        
        # creating a new graph with preserved nodes
        new_graph = graph.subgraph(remaining_nodes)

        return remaining_nodes, new_graph

    except FileNotFoundError:
        print(f"Soubor '{csv_filepath}' nenalezen.")
        return None, None
    except Exception as e:
        print(f"Chyba: {e}")
        return None, None


csv_file = "wolf_relationships.csv"
remaining_nodes, new_graph = minimize_edges_keep_nodes(csv_file)


if remaining_nodes is not None:
    print("Conserved nodes (wolves):", remaining_nodes)
    print("Modified graph (edges):", new_graph.edges())
