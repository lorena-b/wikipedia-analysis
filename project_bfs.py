"""
Graph Class Implementation - Adapted from CSC111 Course Notes
"""
from __future__ import annotations
from typing import Any, Optional
from data import get_direct_links

from main import GOAL, LIMIT


# class Queue:
#     """A first-in-first-out (FIFO) queue of items.
#
#     Stores data in a first-in, first-out order. When removing an item from the
#     queue, the most recently-added item is the one that is removed.
#
#     >>> q = Queue()
#     >>> q.is_empty()
#     True
#     >>> q.enqueue('hello')
#     >>> q.is_empty()
#     False
#     >>> q.enqueue('goodbye')
#     >>> q.dequeue()
#     'hello'
#     >>> q.dequeue()
#     'goodbye'
#     >>> q.is_empty()
#     True
#     """
#     # Private Instance Attributes:
#     #   - _items: The items stored in this queue. The front of the list represents
#     #             the front of the queue.
#     _items: list
#
#     def __init__(self) -> None:
#         """Initialize a new empty queue."""
#         self._items = []
#
#     def is_empty(self) -> bool:
#         """Return whether this queue contains no items.
#         """
#         return self._items == []
#
#     def enqueue(self, item: Any) -> None:
#         """Add <item> to the back of this queue.
#         """
#         self._items.append(item)
#
#     def dequeue(self) -> Optional[Any]:
#         """Remove and return the item at the front of this queue.
#
#         Raise an EmptyQueueError if this queue is empty.
#         """
#         if self.is_empty():
#             raise EmptyQueueError
#         else:
#             return self._items.pop(0)
#
#
# class EmptyQueueError(Exception):
#     """Exception raised when calling dequeue on an empty queue."""
#
#     def __str__(self) -> str:
#         """Return a string representation of this error."""
#         return 'dequeue may not be called on an empty queue'


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

    def get_all_vertices(self) -> set:
        """Return a set of all vertex items in this graph.

        If kind != '', only return the items of the given vertex kind.

        Preconditions:
            - kind in {'', 'user', 'book'}
        """
        return set(self._vertices.keys())

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


def make_graph() -> Graph:
    """Create a graph with the connections to the goal
    """
    g = Graph()
    g.add_vertex(GOAL)

    direct_links = get_direct_links(GOAL, LIMIT)

    for link in direct_links:
        g.add_vertex(link)
        g.add_edge(GOAL, link)

    # need to extend the connections (only has things directly connected to kevin bacon)
    # maybe recursion needs to be used

    return g


# V1

# def bfs_search(self, start_point: _Vertex, end_point: _Vertex) -> str:
#     """
#     Performs a BST search
#     Preconditions:
#         - Input Graph is connected
#     """
#     # search_queue = [start_point.neighbours]
#     # for page in search_queue:
#     #     search_queue.append(page.)
#     # search_queue.append(search_queue[1].neighbours)
#     prev = solve(self, start_point)
#
#     return redo_path(start_point, end_point, prev)
#
#
# def solve(my_graph: Graph(), start_point) -> list:
#     """
#     ...
#     """
#     n = len(Graph.get_all_vertices(my_graph))
#     graph_queue = Queue()
#     graph_queue.enqueue(start_point)
#
#     visited = [False] * n
#     visited[start_point] = True
#     prev = [None] * n
#     while not graph_queue.is_empty():
#         node = graph_queue.dequeue()
#         neighbours = Graph.get_neighbours(my_graph, node)
#         for item in neighbours:
#             if visited[item] is False:
#                 graph_queue.enqueue(item)
#                 visited[item] = True
#                 prev[item] = node
#     return prev
#
# def redo_path(start_point, end_point, prev):
#
#     path = []
#     for

# v2


def bfs2(graph: Graph, start: _Vertex, end: _Vertex) -> Any:
    """Preliminary *non-recursive* BFS implementation
    """
    path_queue = [[start]]
    seen = set()
    while path_queue:
        new_path = path_queue.pop(0)
        curr_node = new_path[-1]
        if curr_node == end:
            return path_queue
        elif curr_node not in seen:
            for item in graph.get_neighbours(curr_node):
                new_path = list(new_path)
                new_path.append(item)
                path_queue.append(new_path)
                seen.add(item)


if __name__ == "__main__":
    import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'max-nested-blocks': 4,
    #     'disable': ['E1136'],
    #     'extra-imports': [],
    #     'allowed-io': []
    # })
