"""
BIM-to-Graph — Graph Factory
============================
Transforms IFC structural hierarchies and logical relationships into
NetworkX Graph objects for topological analysis.
"""

import networkx as nx
import logging
from typing import Optional
from .ifc_adapter import IFCAdapter

logger = logging.getLogger(__name__)

import networkx as nx
import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class GraphFactory:
    """
    Orchestrates the conversion of structural hierarchies into Mathematical Graphs.
    Supports spatial (aggregation) and logical (connectivity) mapping.
    """

    def __init__(self, project_name: str = "BIM_Project"):
        self.project_name = project_name
        self.graph = nx.DiGraph(name=project_name)

    def build_from_relationships(self, relationships: List[Dict[str, Any]]) -> nx.DiGraph:
        """
        Dynamically builds a graph from a list of AEC relationships.
        Expects: {'source': str, 'target': str, 'type': str, 'metadata': dict}
        """
        logger.info(f"Building topological graph for {self.project_name}")
        
        for rel in relationships:
            src = rel.get('source')
            tgt = rel.get('target')
            rel_type = rel.get('type', 'RELATES_TO')
            
            if src and tgt:
                self.graph.add_edge(src, tgt, relation=rel_type, **rel.get('metadata', {}))
                
                # Tag nodes based on identifiers if not already present
                if 'type' not in self.graph.nodes[src]:
                    self.graph.nodes[src]['type'] = self._infer_type(src)
                if 'type' not in self.graph.nodes[tgt]:
                    self.graph.nodes[tgt]['type'] = self._infer_type(tgt)
        
        return self.graph

    def get_impact_nodes(self, source_node: str) -> List[str]:
        """
        Identifies all elements downstream from a node (e.g. supported elements).
        Uses simple Breadth-First Search (BFS).
        """
        if source_node not in self.graph:
            return []
        
        # All nodes reachable from the source (downstream impact)
        return list(nx.descendants(self.graph, source_node))

    def get_centrality_scores(self) -> Dict[str, float]:
        """
        Calculates Betweenness Centrality to identify 'critical' structural nodes.
        Higher score = node sits on more shortest paths through the building.
        """
        return nx.betweenness_centrality(self.graph)

    def _infer_type(self, element_id: str) -> str:
        """Utility to categorize nodes if metadata is missing."""
        id_lower = element_id.lower()
        if 'col' in id_lower: return 'IfcColumn'
        if 'beam' in id_lower: return 'IfcBeam'
        if 'slab' in id_lower: return 'IfcSlab'
        if 'wall' in id_lower: return 'IfcWall'
        return 'IfcProduct'
