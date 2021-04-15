"""
Data Processing Methods

This file is Copyright (c) 2021 Lorena Buciu, Luke Kuo, Aidan Ryan, Kevin Yang
"""
from __future__ import annotations
from typing import Any
from graph import Graph, _Vertex


# BFS ALGORITHM
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
