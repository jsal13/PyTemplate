"""Sample Module."""
import logging
from dataclasses import dataclass
from typing import Optional

from pytemplate.utils import configure_logger

configure_logger()
_logger = logging.getLogger(__name__)


@dataclass(frozen=True, eq=True)
class Node:
    """Node object with ``x`` and ``y`` coordinate and an optional ``value``."""

    x: float
    y: float
    value: Optional[float] = None


@dataclass(frozen=True, eq=True)
class Edge:
    """
    Directed Edge object.

    ``source`` and ``dest`` are the source and destination
    :class:`~pytemplate.module1.Node` of the edge.
    """

    source: Node
    dest: Node


if __name__ == "__main__":
    _logger.info("Running module 1...")
