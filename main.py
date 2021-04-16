"""CSC111 Winter 2021 Final Project: Main Execution

This file culminates all previous work into a single function with customizability
parameters, allowing the user to analyze data in a number of outlined ways through
visual demonstration.

This file is Copyright (c) 2021 Aidan Ryan, Lorena Buciu, Kevin Yang, Kuan-Lin Kuo.
"""
from processing import paths_by_min_connections
from visualizations import connectivity_bar_graph, run_dash_app


def six_degrees(filepath: str = 'graph_data.csv', depth_cap: int = 6,
                analysis_type: str = 'random', target: str = 'Kevin Bacon') -> None:
    """Formats, processes, and visualizes analyses of the given graph.
     Accepts a depth_cap argument that determines the maximum limit for the analysis to
     help with runtime on larger graphs.
     Accepts an analysis_type argument that determines which analysis is performed:
            - 'random' = Randomly choose a vertex as the starting point to connect to target
            - 'full' = Uses all vertices in graph to analyse widespread connectivity to target.
                       The runtime for this will be significantly longer!
    There is a lot of possible experimentation here! Please, see the final report for more
    specific details.

    Preconditions
        - target in graph.get_all_vertices()
        - analysis_type in {'random', 'full'}
        - depth_cap > 0
        - filepath is the path to a CSV file containing wikipedia article and connection using the
        same format as the data in data/Wikipedia_test_data.csv.
    """
    if analysis_type == 'random':
        run_dash_app(filepath, depth_cap, target)
    else:  # analysis_type == 'full'
        paths = paths_by_min_connections()
        connectivity_bar_graph(paths).show()


if __name__ == '__main__':
    six_degrees(filepath='graph_data.csv', analysis_type='random')
