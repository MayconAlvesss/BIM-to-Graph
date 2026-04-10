"""
BIM-to-Graph — Visualization Engine
===================================
Exports geometric-driven graph representations for CAD systems or 
web visualizations (D3.js / Pyvis).
"""

import networkx as nx
import matplotlib.pyplot as plt
import logging
import os

logger = logging.getLogger(__name__)

def export_to_graphml(graph: nx.DiGraph, filename: str = "building_network.graphml"):
    """
    Exports the NetworkX graph to industry-standard GraphML format.
    """
    try:
        nx.write_graphml(graph, filename)
        logger.info(f"Successfully exported graph to {filename}")
    except Exception as e:
        logger.error(f"Failed to export GraphML: {e}")

def plot_topology(graph: nx.DiGraph, output_img: str = "topology_map.png"):
    """
    Generates a high-resolution topology map of the building logic.
    """
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph, seed=42)
    
    nx.draw(
        graph, pos, 
        with_labels=True, 
        node_color='skyblue', 
        node_size=2000, 
        edge_color='gray', 
        arrowsize=20, 
        font_size=10
    )
    
    plt.title("AEC Structural Connectivity Graph")
    plt.savefig(output_img)
    plt.close()
    logger.info(f"Topology map saved to {output_img}")

if __name__ == "__main__":
    # Test logic
    G = nx.DiGraph()
    G.add_edge("Column_A", "Beam_B")
    G.add_edge("Beam_B", "Slab_C")
    plot_topology(G)
