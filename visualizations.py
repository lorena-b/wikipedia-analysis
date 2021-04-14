"""
Graph Visualization Methods
"""
import networkx as nx
from plotly.graph_objs import Scatter, Figure
from Graph import Graph


# Show smallest path
def smallest_path() -> None:
    """Display a tree of the smallest path to kevin bacon from a random wikipedia
    article
    """


# Show whole graph
def visualize_graph(g: Graph) -> None:
    """Display the graph showing the article links
    """
    nx_graph = g.to_networkx()





if __name__ == "__main__":
    import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'max-nested-blocks': 4,
    #     'disable': ['E1136'],
    #     'extra-imports': [],
    #     'allowed-io': []
    # })
