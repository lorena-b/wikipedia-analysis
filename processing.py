"""CSC111 Winter 2021 Final Project: Data Processing

This file contains any code needed to read and format data, as well as process it for
visualization.

This file is Copyright (c) 2021 Aidan Ryan, Lorena Buciu, Kevin Yang, Kuan-Lin Kuo.
"""
import csv
from graph import Graph


def read_csv_data(filepath: str) -> dict[str, list[str]]:
    """Return a dictionary that has a formatted version of the given .csv data, where the keys are
    all of the wikipedia pages in the dataset and the values associated with those keys
    are the pages directly linked to the key page.
    Runtime would likely be faster directly creating a dictionary from this data, but
    there would be a lot of nesting of if statements and loops to do so properly.

    With an ideal dataset, any items that appear in the dictionary values would also appear as
    keys.

    Preconditions:
        - filepath is the path to a CSV file containing wikipedia article and connection using the
          same format as the data in data/Wikipedia_test_data.csv.
        - there are no duplicate article names in the first header column (article titles) of the
          dataset.
    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        dict_so_far = {}
        for row in reader:
            dict_so_far[row[0]] = row[1].split(', ')  # row[0] not in dict_so_far, from precondition
    return dict_so_far


def create_wiki_graph(article_connections: dict[str, list[str]]) -> Graph:
    """Return a wiki graph based on the given dictionary."""
    wiki_graph = Graph()
    main_articles = article_connections.keys()

    for article in main_articles:
        if article not in wiki_graph.get_all_vertices():
            wiki_graph.add_vertex(article)

        for connected_article in article_connections[article]:
            if connected_article not in wiki_graph.get_all_vertices():
                wiki_graph.add_vertex(connected_article)
            wiki_graph.add_edge(article, connected_article)
    return wiki_graph


def bfs_record(graph: Graph, start: str, target: str, depth_cap: int = 6) -> list:
    """Returns a list representing the shortest path found by breadth first search algorithm,
     in order. This implementation is iterative, not recursive, as it better facilitates
     this path tracing.
     Accepts a depth_cap argument that sets a limit for how deep the algorithm searches for
     connections. Runtimes seem fine without a cap, but this should help with much denser data.

    Preconditions:
        - start in graph.get_all_vertices
        - depth_cap > 0
    """
    queue = [(start, [start])]
    visited = set()
    path = []

    if start == target:
        return [start]

    while len(path) <= depth_cap and queue:
        article, path = queue.pop(0)
        visited.add(article)
        for connected_article in graph.get_neighbours(article):
            if connected_article == target:
                return path + [target]
            elif connected_article not in visited:
                visited.add(connected_article)
                queue.append((connected_article, path + [connected_article]))
            else:
                pass
    return []  # occurs when no path is reached before hitting depth cap


def paths_by_min_connections(filepath: str = 'graph_data.csv',
                             target: str = 'Kevin Bacon',
                             depth_cap: int = 6) -> dict[int, list[list[str]]]:
    """Takes a list of articles"""
    wiki = create_wiki_graph(read_csv_data(filepath))
    articles = wiki.get_all_vertices()

    paths = {}
    for article in articles:
        path = bfs_record(wiki, article, target, depth_cap)
        if len(path) not in paths:
            paths[len(path)] = [path]
        else:
            paths[len(path)].append(path)
    return paths


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'csv', 'graph'],
        'allowed-io': ['read_csv_data'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
