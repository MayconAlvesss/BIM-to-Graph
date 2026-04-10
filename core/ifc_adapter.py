"""
BIM-to-Graph — IFC Adapter
==========================
Wrapper for ifcopenshell to simplify spatial and relationship queries
needed for graph construction.
"""

import logging
from typing import List, Any

# Mocking ifcopenshell
try:
    import ifcopenshell
except ImportError:
    ifcopenshell = None

logger = logging.getLogger(__name__)

class IFCAdapter:
    """
    Abstractions over the raw IFC schema for graph-specific extraction.
    """

    def __init__(self, path: str):
        self.path = path
        self.model = None
        self._load()

    def _load(self):
        if ifcopenshell:
            try:
                self.model = ifcopenshell.open(self.path)
            except Exception as e:
                logger.error(f"Failed to load IFC: {e}")

    def get_spatial_tree(self) -> List[Any]:
        """
        Extracts the spatial hierarchy (Project -> Site -> Building).
        """
        if not self.model:
            return []
        
        return self.model.by_type("IfcBuilding")

    def get_connections(self, element: Any) -> List[Any]:
        """
        Finds all elements physically connected to the given element.
        """
        # Logic to follow IfcRelConnectsElements
        return []
