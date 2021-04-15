"""
Graph Class Implementation and construction functions

This file is Copyright (c) 2021 Lorena Buciu, Luke Kuo, Aidan Ryan, Kevin Yang
"""
from __future__ import annotations
from typing import Any

import networkx as nx

from data import get_direct_links


# Classes Adapted from CSC111 Course Notes and A3
class _Vertex:
    """A vertex in a graph.
    Instance Attributes:
        - item: The data stored in this vertex.
        - neighbours: The vertices that are adjacent to this vertex.
    Preconditions:
        - self not in self.neighbours
        - all(self in n.neighbours for n in self.neighbours)
    """
    item: Any
    neighbours: set[_Vertex]

    def __init__(self, item: Any, neighbours: set[_Vertex]) -> None:
        """Initialize a new vertex with the given item and neighbours."""
        self.item = item
        self.neighbours = neighbours


class Graph:
    """A graph.
    """
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps item to _Vertex object.
    _vertices: dict[Any, _Vertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def add_vertex(self, item: Any) -> None:
        """Add a vertex with the given item to this graph.
        The new vertex is not adjacent to any other vertices.
        Preconditions:
            - item not in self._vertices
        """
        self._vertices[item] = _Vertex(item, set())

    def add_edge(self, item1: Any, item2: Any) -> None:
        """Add an edge between the two vertices with the given items in this graph.
        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.
        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            # Add the new edge
            v1.neighbours.add(v2)
            v2.neighbours.add(v1)
        else:
            # We didn't find an existing vertex for both items.
            raise ValueError

    def adjacent(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are adjacent vertices in this graph.

        Return False if item1 or item2 do not appear as vertices in this graph.
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            return any(v2.item == item2 for v2 in v1.neighbours)
        else:
            return False

    def get_neighbours(self, item: Any) -> set:
        """Return a set of the neighbours of the given item.

        Note that the *items* are returned, not the _Vertex objects themselves.

        Raise a ValueError if item does not appear as a vertex in this graph.
        """
        if item in self._vertices:
            v = self._vertices[item]
            return {neighbour.item for neighbour in v.neighbours}
        else:
            raise ValueError

    def get_all_vertices(self) -> set:
        """Return a set of all vertex items in this graph.
        """
        return set(self._vertices.keys())

    def to_networkx(self) -> nx.Graph:
        """Convert the graph into an nx.graph object to use
        for plotly visualization
        """
        nx_graph = nx.Graph()

        for v in self._vertices:
            nx_graph.add_node(self._vertices[v].item)

            for u in self._vertices[v].neighbours:
                nx_graph.add_node(u.item)

                if u.item in nx_graph.nodes:
                    nx_graph.add_edge(u.item, self._vertices[v].item)

        return nx_graph

    def get_vertex(self, goal: Any):
        """Return the specified vertex object
        """
        return self._vertices[goal]


# Graph construction functions
def make_graph(goal: str, limit: int, depth: int) -> Graph:
    """Create a graph with the connections to the goal
    """
    print('Creating Graph...')
    g = Graph()
    g.add_vertex(goal)

    direct_links = get_direct_links(goal, limit)
    extend(g, depth, goal, direct_links, limit)

    print('Graph has been created.')
    return g


def extend(graph: Graph, d: int, link: str, link_list: list, limit: int) -> None:
    """Extend the graph up to a max connection depth of d
    """
    if d == 0:
        pass
    else:
        for links in link_list:
            if links not in graph.get_all_vertices():
                graph.add_vertex(links)

            graph.add_edge(link, links)
            direct_links = get_direct_links(links, limit)
            extend(graph, d - 1, links, direct_links, limit)


if __name__ == "__main__":
    import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'max-nested-blocks': 4,
    #     'disable': ['E1136'],
    #     'extra-imports': [],
    #     'allowed-io': []
    # })
