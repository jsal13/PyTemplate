"""Create Graph Object from the Node and Edge objects in `module1`."""
import logging

from pytemplate.module1 import Edge, Node
from pytemplate.utils import configure_logger

configure_logger()
_logger = logging.getLogger(__name__)


class Graph:
    """
    Graph consisting of nodes and edges.

    Attributes
    ----------
    nodes : list[:class:`~pytemplate.module1.Node`]
        Nodes in the graph
    edges : list[:class:`~pytemplate.module1.Edge`]
        Directed edges in the graph
    """

    def __init__(self, nodes: list[Node], edges: list[Edge]):
        """
        Graph consisting of nodes and edges.

        Parameters
        ----------
        nodes : list[:class:`~pytemplate.module1.Node`]
            Nodes in the graph
        edges : list[:class:`~pytemplate.module1.Edge`]
            Directed edges in the graph
        """
        self.nodes = nodes
        self.edges = edges

    def count_nodes(self):
        """Compute the number of ``nodes``."""
        _logger.info("Look at all those nodes!")
        return len(self.nodes)

    def has_an_edge(self, source: Node, dest: Node) -> bool:
        """
        Check to see if there is an edge between ``source`` and ``dest``.

        Parameters
        ----------
        source : :class:`~pytemplate.module1.Node`
            Source node to check
        dest : :class:`~pytemplate.module1.Node`
            Destination node to check


        Returns
        -------
        bool
        """
        for edge in self.edges:
            if edge.source == source and edge.dest == dest:
                return True
        return False


if __name__ == "__main__":
    _nodes = [Node(0, 0, 1), Node(0, 1, 1), Node(1, 0, 1), Node(1, 1, 1)]
    _edges = [Edge(_nodes[0], _nodes[1]), Edge(_nodes[1], _nodes[2])]
    _graph = Graph(_nodes, _edges)

    _graph.count_nodes()
