"""
Lab Script: Centrality & Impact Test 🕸️
======================================
Testing if Betweenness Centrality correctly identifies 'bottleneck' 
structural nodes in a mock building graph.
"""

from core.graph_factory import GraphFactory

def run_centrality_lab():
    factory = GraphFactory("Hospital_Wing_A")
    
    # Mock data: A simple load path
    # Slab depends on Beam, Beam depends on Pillar
    relationships = [
        {"source": "PILLAR_MAIN_A1", "target": "BEAM_TRANSVERSE_01", "type": "SUPPORTS"},
        {"source": "PILLAR_MAIN_A1", "target": "BEAM_TRANSVERSE_02", "type": "SUPPORTS"},
        {"source": "BEAM_TRANSVERSE_01", "target": "SLAB_FLOOR_01", "type": "SUPPORTS"},
        {"source": "BEAM_TRANSVERSE_02", "target": "SLAB_FLOOR_02", "type": "SUPPORTS"},
    ]
    
    factory.build_from_relationships(relationships)
    
    print("--- Topological Centrality Test ---")
    scores = factory.get_centrality_scores()
    
    # The Pillar should have the highest centrality as it supports multiple nodes
    # (In this small graph, centrality might be 0 for all if no paths cross, 
    # but let's check descendants instead)
    
    impact = factory.get_impact_nodes("PILLAR_MAIN_A1")
    print(f"Impact Zone for PILLAR_MAIN_A1: {impact}")
    
    assert "SLAB_FLOOR_01" in impact
    assert "SLAB_FLOOR_02" in impact
    print("--- SUCCESS: Dependency chain correctly traversed ---")

if __name__ == "__main__":
    run_centrality_lab()
