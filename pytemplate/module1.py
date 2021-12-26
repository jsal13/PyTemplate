"""Sample Module."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, eq=True)
class Node:
    """Node object.

    Parameters
    ----------
    x : float
        x coordinate
    y : float
        y coordinate
    value : Optional[float]
        value or cost for the node
    """

    x: float
    y: float
    value: Optional[float] = None


@dataclass(frozen=True, eq=True)
class Edge:
    """Directed Edge object.

    Parameters
    ----------
    source: Node
        Source node for the directed edge.
    dest: Node:
        Destination node for the directed edge.
    """

    source: Node
    dest: Node
