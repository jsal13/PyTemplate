"""Create Graph Object from the Node and Edge objects in `module1`."""

from pytemplate.module1 import Node, Edge


class Graph:
    """Graph object containing `nodes` and `edges`.

    Parameters
    ----------
    nodes : list[Node]
        List of nodes to include.
    edges : list[Edge]
        List of (directed) edges to include.
    """

    def __init__(self, nodes: list[Node], edges: list[Edge]):
        self.nodes = nodes
        self.edges = edges

    def count_nodes(self):
        """Counts the number of nodes."""
        return len(self.nodes)

    def has_an_edge(self, source: Node, dest: Node) -> bool:
        """Checks to see if there is an edge between `source` and `dest.`

        Parameters
        ----------
        source : Node
        dest : Node

        Returns
        -------
        bool
        """

        for edge in self.edges:
            if edge.source == source and edge.dest == dest:
                return True
        return False
