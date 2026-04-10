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

class GraphFactory:
    """
    Orchestrates the conversion of BIM models into Mathematical Graphs.
    """

    def __init__(self, ifc_path: str):
        self.ifc_adapter = IFCAdapter(ifc_path)
        self.graph = nx.DiGraph() # Directed graph to represent load/flow

    def build_spatial_graph(self) -> nx.DiGraph:
        """
        Builds a graph based on spatial aggregation (Project -> Site -> Building -> etc).
        """
        logger.info("Initializing Spatial Graph construction...")
        
        # Placeholder for extraction logic
        self.graph.add_node("Root", label="IfcProject", type="Logical")
        self.graph.add_node("Level_0", label="IfcBuildingStorey", type="Spatial")
        self.graph.add_edge("Root", "Level_0", relation="Contains")
        
        # Adding some elements
        elements = ["Wall_01", "Beam_01", "Col_01"]
        for el in elements:
            self.graph.add_node(el, label="IfcProduct", type="Physical")
            self.graph.add_edge("Level_0", el, relation="Contains")
            
        return self.graph

    def build_connectivity_graph(self) -> nx.DiGraph:
        """
        Builds a graph based on physical connectivity (e.g. Beam connects to Column).
        """
        # Logic to parse IfcRelConnects
        self.graph.add_edge("Beam_01", "Col_01", relation="Connects")
        return self.graph
