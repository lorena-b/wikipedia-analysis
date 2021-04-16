"""
CSC111 Final Project - Analyzing Wikipedia Connectivity to Kevin Bacon

This is the main module, it will:
    - Create the network graph
    - Perform computations on the graph
    - Produce a Dash webpage output of the visualizations

This file is Copyright (c) 2021 Lorena Buciu, Luke Kuo, Aidan Ryan, Kevin Yang
"""
from processing import create_wiki_graph, read_csv_data
from visualizations import connectivity_bar_graph, run_dash_app


def six_degrees(filepath: str = 'data/Wikipedia_test_data.csv', depth_cap: int = 6,
                analysis_type: str = 'random', target: str = 'Kevin Bacon') -> None:
    """Formats, processes, and visualizes analyses of the given graph.
     Accepts a depth_cap argument that determines the maximum limit for the analysis to
     help with runtime on larger graphs.
     Accepts an analysis_type argument that determines which analysis is performed:
            - 'random' = Randomly choose a vertex as the starting point to connect to target
            - 'full' = Uses all vertices in graph to analyse widespread connectivity to target.
                       The runtime for this will be significantly longer!
    There is a lot of possible experimentation here!

    Preconditions
        - target in graph.get_all_vertices()
        - analysis_type in {'random', 'full'}
        - depth_cap > 0
        - filepath is the path to a CSV file containing wikipedia article and connection using the
          same format as the data in data/Wikipedia_test_data.csv.
    """
    wiki = create_wiki_graph(read_csv_data(filepath))
    articles = wiki.get_all_vertices()

    if analysis_type == 'random':
        run_dash_app(filepath, depth_cap, target)
    else:  # analysis_type == 'full'
        paths = {}
        for i in range(len(articles)):
            ...
        connectivity_bar_graph(paths)


if __name__ == '__main__':
    six_degrees(filepath='graph_data.csv', analysis_type='random')
