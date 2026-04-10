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

    def find_critical_path(self) -> List[str]:
        """
        Identifies elements with high centrality - nodes that link
        multiple systems together (e.g. main structural cores).
        """
        # Centrality analysis using betweenness
        centrality = nx.betweenness_centrality(self.graph)
        sorted_centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
        
        return [item[0] for item in sorted_centrality[:5]]
