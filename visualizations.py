"""
Graph Visualization Methods
"""
import networkx as nx
from plotly.graph_objs import Scatter, Figure
import plotly.graph_objects as go
from graph import Graph, make_graph
from processing import bfs2


# Show smallest path
def smallest_path() -> None:
    """Display a tree of the smallest path to kevin bacon from a random wikipedia
    article
    """


# Show whole graph
def visualize_graph(g: Graph) -> None:
    """Display the graph showing the article links
    Adapted from A3
    """
    graph_nx = g.to_networkx()

    pos = getattr(nx, 'spring_layout')(graph_nx)

    x_values = [pos[k][0] for k in graph_nx.nodes]
    y_values = [pos[k][1] for k in graph_nx.nodes]
    labels = list(graph_nx.nodes)

    x_edges = []
    y_edges = []
    for edge in graph_nx.edges:
        x_edges += [pos[edge[0]][0], pos[edge[1]][0], None]
        y_edges += [pos[edge[0]][1], pos[edge[1]][1], None]

    trace3 = Scatter(x=x_edges,
                     y=y_edges,
                     mode='lines',
                     name='edges',
                     line=dict(width=1),
                     hoverinfo='none',
                     )
    trace4 = Scatter(x=x_values,
                     y=y_values,
                     mode='markers',
                     name='nodes',
                     marker=dict(symbol='circle-dot',
                                 size=5,
                                 line=dict(width=0.5)
                                 ),
                     text=labels,
                     hovertemplate='%{text}',
                     hoverlabel={'namelength': 0}
                     )

    data1 = [trace3, trace4]
    fig = Figure(data=data1)
    fig.update_layout({'showlegend': False})
    fig.update_xaxes(showgrid=False, zeroline=False, visible=False)
    fig.update_yaxes(showgrid=False, zeroline=False, visible=False)

    fig.show()


def connectivity_bar_graph() -> None:
    """Display a bar graph with the widespread connections data
    """


if __name__ == "__main__":
    # test
    graph = make_graph()
    visualize_graph(graph)
    import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'max-nested-blocks': 4,
    #     'disable': ['E1136'],
    #     'extra-imports': [],
    #     'allowed-io': []
    # })
