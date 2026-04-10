"""
BIM-to-Graph — Impact Engine
============================
Structural and logical impact analysis using graph traversal algorithms.
Predicts how changes to one element propagate through the building system.
"""

import networkx as nx
import logging
from typing import List, Set

logger = logging.getLogger(__name__)

class ImpactEngine:
    """
    Analyzes the 'Ripple Effect' of BIM modifications using BFS/DFS.
    """

    def __init__(self, graph: nx.DiGraph):
        self.graph = graph

    def simulate_deletion(self, start_node: str) -> Set[str]:
        """
        Uses Breadth-First Search (BFS) to find all downstream elements
        that depend on the specified node.
        """
        if start_node not in self.graph:
            logger.warning(f"Node {start_node} not found in graph.")
            return set()

        # Find all reachable nodes in a directed graph (Impact Zone)
        impacted = nx.descendants(self.graph, start_node)
        
        logger.info(f"Deletion of {start_node} impacts {len(impacted)} elements.")
        return impacted

    def find_critical_path(self) -> List[Dict[str, Any]]:
        """
        Identifies elements with high centrality - nodes that link
        multiple systems together (e.g. main structural cores).
        Uses industry-standard betweenness centrality algorithms.
        """
        if not self.graph.nodes:
            return []

        # Centrality analysis using betweenness (Structural bottleneck detection)
        centrality = nx.betweenness_centrality(self.graph)
        degree = dict(self.graph.degree())
        
        results = []
        for node in centrality:
            results.append({
                "node_id": node,
                "centrality": round(centrality[node], 4),
                "connections": degree[node],
                "is_hub": centrality[node] > 0.5
            })
            
        # Sort by importance
        results.sort(key=lambda x: x['centrality'], reverse=True)
        return results[:10]
