"""CSC111 Winter 2021 Final Project: Data Visualization

This file contains any code needed to visualize the formatted and processed data.

This file is Copyright (c) 2021 Aidan Ryan, Lorena Buciu, Kevin Yang, Kuan-Lin Kuo.
"""
import random
import networkx as nx
from plotly.graph_objs import Figure, Scatter

from graph import Graph
from processing import bfs_record, read_csv_data, create_wiki_graph

GOAL_COLOUR = 'rgb(255, 0, 0)'
V_COLOUR = 'rgb(0, 0, 255)'

GOAL_SIZE = 15
V_SIZE = 10


# Show smallest path
def smallest_path(goal: str, csv: str) -> Figure:
    """Display a visual of the smallest path to kevin bacon from a random wikipedia
    article
    
    Preconditions:
        - goal in csv
    """
    data = read_csv_data(csv)
    g = create_wiki_graph(data)
    graph_nx = g.to_networkx()

    pos = nx.spring_layout(graph_nx)

    # Don't use the goal as the starting node
    start = random.choice(g.get_all_vertices())
    while start == goal:
        start = random.choice(g.get_all_vertices())

    shortest_path = bfs_record(g, start, target=goal)

    x_values = [pos[k][0] for k in graph_nx.nodes]
    y_values = [pos[k][1] for k in graph_nx.nodes]
    labels = list(graph_nx.nodes)

    colours = [GOAL_COLOUR if node in shortest_path else V_COLOUR for node in graph_nx.nodes]
    sizes = [GOAL_SIZE if node == goal or node in shortest_path else V_SIZE
             for node in graph_nx.nodes]

    x_edges = []
    y_edges = []
    for edge in graph_nx.edges:
        x_edges += [pos[edge[0]][0], pos[edge[1]][0], None]
        y_edges += [pos[edge[0]][1], pos[edge[1]][1], None]

    edges = Scatter(x=x_edges,
                    y=y_edges,
                    mode='lines',
                    name='edges',
                    line=dict(color='rgb(0, 0, 0)', width=1),
                    hoverinfo='none',
                    )
    nodes = Scatter(x=x_values,
                    y=y_values,
                    mode='markers',
                    name='nodes',
                    marker=dict(symbol='circle-dot',
                                size=sizes,
                                line=dict(width=0.5),
                                color=colours,
                                opacity=1),
                    text=labels,
                    hovertemplate='%{text}',
                    hoverlabel={'namelength': 0}
                    )

    data1 = [edges, nodes]
    fig = Figure(data=data1)
    fig.update_layout(title=f"Graph displaying one of "
                            f"the shortest paths to {goal} from "
                            f"{start} (length: {len(shortest_path)})")
    fig.update_layout({'showlegend': False})
    fig.update_xaxes(showgrid=False, zeroline=False, visible=False)
    fig.update_yaxes(showgrid=False, zeroline=False, visible=False)

    return fig


# Show whole graph, only used for testing
def visualize_graph(g: Graph, goal: str, limit: int, depth: int) -> Figure:
    """Display the graph showing the article links
    Adapted from A3.

    Preconditions:
        - limit > 0
        - depth > 0
    """
    graph_nx = g.to_networkx()

    pos = nx.spring_layout(graph_nx)

    x_values = [pos[k][0] for k in graph_nx.nodes]
    y_values = [pos[k][1] for k in graph_nx.nodes]
    labels = list(graph_nx.nodes)

    colours = [GOAL_COLOUR if node == goal else V_COLOUR for node in graph_nx.nodes]
    sizes = [GOAL_SIZE if node == goal else V_SIZE for node in graph_nx.nodes]

    x_edges = []
    y_edges = []
    for edge in graph_nx.edges:
        x_edges += [pos[edge[0]][0], pos[edge[1]][0], None]
        y_edges += [pos[edge[0]][1], pos[edge[1]][1], None]

    edges = Scatter(x=x_edges,
                    y=y_edges,
                    mode='lines',
                    name='edges',
                    line=dict(color='rgb(0, 0, 0)', width=1),
                    hoverinfo='none',
                    )
    nodes = Scatter(x=x_values,
                    y=y_values,
                    mode='markers',
                    name='nodes',
                    marker=dict(symbol='circle-dot',
                                size=sizes,
                                line=dict(width=0.5),
                                color=colours,
                                opacity=1),
                    text=labels,
                    hovertemplate='%{text}',
                    hoverlabel={'namelength': 0}
                    )

    data1 = [edges, nodes]
    fig = Figure(data=data1)
    fig.update_layout(title=f"Graph displaying "
                            f"the connections to {goal} (limit: {limit}, depth: {depth})")
    fig.update_layout({'showlegend': False})
    fig.update_xaxes(showgrid=False, zeroline=False, visible=False)
    fig.update_yaxes(showgrid=False, zeroline=False, visible=False)

    return fig


def connectivity_bar_graph() -> Figure:
    """Display a bar graph with the widespread connections data
    """


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'max-nested-blocks': 4,
        'disable': ['E1136'],
        'extra-imports': ['networkx', 'plotly.graph_objs', 'graph', 'random', 'processing'],
        'allowed-io': []
    })
