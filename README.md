<p align="center">
  <img src="https://img.icons8.com/wired/128/007ACC/network.png" width="80" />
</p>



# <p align="center">BIM-to-Graph</p>

> [!IMPORTANT]
> **Project Status: Concept / Scaffold (2028+)**
> This repository is part of Maycon Alves' technical vision for the AEC Tech ecosystem. It is currently in the **concept and initial architecture phase**. Full development and core implementation will resume after the author returns from his mission in **2028**.


<p align="center">
  <strong>Transforming Hierarchical BIM Data into Topological Networks.</strong><br>
  A mathematical engine for mapping spatial, logical, and structural relationships within AEC assets.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Architecture-Graph_Theory-007ACC?style=flat-square" />
  <img src="https://img.shields.io/badge/Engine-NetworkX-007ACC?style=flat-square" />
  <img src="https://img.shields.io/badge/Interop-OpenBIM-007ACC?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Functional_Beta-444444?style=flat-square" />
</p>

---

## 🛰️ Topological Foundation
BIM-to-Graph captures the "living" performance of a building. While traditional BIM tools focus on geometry, this engine extracts **Structural Centrality** and **Load Path Continuity**, treating the building as a relational graph $G = (V, E)$.

### Key Analytical Capabilities
- **Spatial Aggregation**: Resolving building storeys and zones into a hierarchy of connected nodes.
- **Impact Simulation**: Analyzing the "Impact Zone" of a deleted or modified structural element through graph traversal.
- **Dependency Mapping**: Identifying "Single Points of Failure" in MEP and structural systems.

## 🏗️ Implementation Layers

### 1. The Factory (`/core`)
The **`graph_factory.py`** engine handles the conversion of hierarchical data into a unified `NetworkX` directed graph.

### 2. The Impact Engine (`/analysis`)
Advanced algorithms for simulating failures and performance metrics:
- **Centrality Scores**: Identifying critical structural bottlenecks.
- **Connectivity Traversal**: BFS/DFS based impact tracking.

### 3. The Topology Lab (`/lab`)
- **`centrality_test.py`**: A sandbox for testing structural metrics on mock building graphs.

---

## ⚡ Quick Usage

```python
from core.graph_factory import GraphFactory

# 1. Initialize and Load relationships
factory = GraphFactory("Digital_Twin_A")
factory.build_from_relationships(raw_data)

# 2. Analyze Structural Bottlenecks
scores = factory.get_centrality_scores()
print(f"Most critical element: {max(scores, key=scores.get)}")
```

---
<p align="center">
  <i>Part of the <b>Nexus-Twin</b> Ecosystem | Engineering Strategy by <b>Maycon Alves</b></i>
</p>
