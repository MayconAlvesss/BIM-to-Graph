# BIM-to-Graph 🕸️ — Global Network Analysis for Buildings

> **Transforming hierarchical BIM models into high-density Graph Databases. Optimized for universal structural pathfinding and systemic AEC relationship mapping.**

---

## 🛠️ Status: Alpha Prototype (Active Development)

> **Graph Engine Core Ready.** Implements the conversion logic from IFC (OpenBIM) to NetworkX graph structures. Featuring advanced centrality analysis for structural bottleneck detection. Designed for global large-scale master-planning logic.

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| **IFC-to-Graph Mapper** | Automated conversion of spatial (`IfcRelAggregates`) and logical relationships to nodes and edges |
| **Impact Analysis** | Calculates the "Impact Zone" of a deleted or modified element through transitive relationship traversal |
| **System Connectivity** | Maps MEP-to-Structure dependencies for clash and maintenance impact prediction |
| **Structural Topology** | Evaluates load-path continuity using graph-theory algorithms (Connectivity, Centrality) |
| **Neo4j Integration** | Plug-and-play adapter for exporting local NetworkX graphs to Enterprise Neo4j clusters |

---

## 🛠️ Technical Stack

| Layer | Technology |
|---|---|
| **Graph Logic** | Python 3.12, NetworkX |
| **BIM Loader** | `ifcopenshell` |
| **Database** | Neo4j / Memgraph (Optional) |
| **Persistence** | GraphML / JSON |
| **Visualization** | Matplotlib / Pyvis |

---

## 📂 Project Structure

```text
BIM-to-Graph/
├── core/                        # Graph generation core
│   ├── graph_factory.py         # IFC classes to NetworkX nodes/edges
│   └── ifc_adapter.py           # ifcopenshell wrapper for spatial queries
│
├── analysis/                    # Graph algorithms
│   ├── impact_engine.py         # Ripple-effect and dependency analysis
│   └── pathfinding.py           # MEP and egress route optimization
│
├── utils/                       # Shared logic
│   └── topology.py              # Geometric proximity and connectivity helpers
│
├── config/                      # Settings
│   └── thresholds.py            # Weights for graph edges and impact scores
│
├── tests/                       # Validation
│   └── test_graph_logic.py      # Connectivity and traversal unit tests
│
├── requirements.txt             # Project dependencies
└── README.md                    # Professional documentation
```

---

## ⚡ Quick Start

### Step 1 — Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 2 — Generate Building Graph

```python
from core.graph_factory import GraphFactory

# Load IFC and generate graph
factory = GraphFactory("pavilion_structure.ifc")
graph = factory.build_spatial_graph()

# Analyze impact of deleting a column
from analysis.impact_engine import ImpactEngine
analyzer = ImpactEngine(graph)
affected = analyzer.simulate_deletion("COL-101")

print(f"Affected elements: {len(affected)}")
```

---

## 🗺️ Roadmap

- [x] **IFC Schema Mapper** — Basic mapping of `IfcWall`, `IfcBeam`, and `IfcColumn` to nodes
- [x] **Spatial Graph** — Traversal of `Decomposes` and `Contains` relationships
- [x] **Impact Engine** — Basic BFS traversal for structural dependency tracking
- [ ] **MEP Network Mapping** — Detailed flow-direction graph for HVAC and Plumbing
- [ ] **Structural Failure Sim** — Integration with Finite Element (FEM) data for failure propagation
- [ ] **Web Dashboard** — 3D Graph visualization using D3.js or React Force-Graph

---

## 📄 License

Developed for professional recruitment and AEC research purposes.  
See internal documentation for specific licensing terms.

---

<div align="center">
  <b>Visualizing the building as a living, connected neural network.</b>
  <br><br>
  <i>💡 Architecture & Engineering by <b>Maycon Alves</b></i>
  <br>
  <a href="https://github.com/MayconAlvesss" target="_blank">GitHub</a> | <a href="https://www.linkedin.com/in/maycon-alves-a5b9402bb/" target="_blank">LinkedIn</a>
</div>
