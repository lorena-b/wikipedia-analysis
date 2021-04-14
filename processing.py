"""
Analysis Methods
"""
from __future__ import annotations
from typing import Any, Optional
from graph import Graph, _Vertex
from queue_class import Queue


# BFS ALGORITHM
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

# V2
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
    python_ta.check_all(config={
        'max-line-length': 100,
        'max-nested-blocks': 4,
        'disable': ['E1136'],
        'extra-imports': [],
        'allowed-io': []
    })
