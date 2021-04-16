"""CSC111 Winter 2021 Final Project: Data Visualization

This file contains any code needed to visualize the formatted and processed data.

This file is Copyright (c) 2021 Aidan Ryan, Lorena Buciu, Kevin Yang, Kuan-Lin Kuo.
"""
import random
import networkx as nx
from plotly.graph_objs import Figure, Scatter, Bar

from graph import Graph
from processing import bfs_record, read_csv_data, create_wiki_graph

GOAL_COLOUR = 'rgb(255, 135, 54)'
V_COLOUR = 'rgb(22, 163, 245)'

GOAL_SIZE = 15
V_SIZE = 10


# Show smallest path
def smallest_path(goal: str, csv: str) -> Figure:
    """Display a visual of the smallest path to a goal article from a random wikipedia
    article.
    The csv argument represents the filepath of a .csv dataset in the same format as
    data/Wikipedia_test_data.csv.

    Preconditions:
        - The goal article is an article in the dataset specified by the csv filepath
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

    if shortest_path == []:  # this is only returned by bfs_record() if no path is found
        print('No path found between ' + start + ' and ' + goal +
              ' with the chosen depth cap.')
        title = f"No path found with the chosen depth cap to {goal} from {start}"
    else:
        print('A path was found between ' + start + ' and ' + goal +
              ' with the chosen depth cap!')
        title = f"Graph displaying one of the shortest paths to {goal} from " \
                f"{start} (length: {len(shortest_path)})"

    x_values = [pos[k][0] for k in graph_nx.nodes]
    y_values = [pos[k][1] for k in graph_nx.nodes]
    labels = list(graph_nx.nodes)

    colours = [GOAL_COLOUR if node in shortest_path
               else V_COLOUR for node in graph_nx.nodes]
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
    fig.update_layout(title=title)
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


def connectivity_bar_graph(paths: dict[int, list[list[str]]]) -> Figure:
    """Returns a bar graph comparing the minimum number of connections required (to connect
    a start article to the target) and the number of starting articles that require that
    minimum amount.
    """
    fig = Figure()
    x, y = list(paths.keys()), axis_calculator(paths)
    hovertext = hovertext_formatter(paths)

    custom_scale = [[0, "rgb(255, 229, 54)"],
                    [0.25, "rgb(255, 195, 54)"],
                    [0.5, "rgb(255, 168, 54)"],
                    [1.0, "rgb(255, 135, 54)"]]

    fig.add_trace(Bar(x=x, y=y, hovertext=hovertext,
                      marker=dict(color=y, colorscale=custom_scale)))

    fig.update_layout(title='Full Analysis of Wikipedia Connectivity to Target',
                      xaxis_title='Minimum Number of Required Connections',
                      yaxis_title='Number of Articles')

    return fig


def axis_calculator(paths: dict[int, list[list[str]]]) -> list[int]:
    """Returns list containing axis values for bar graph, based on the number of articles
    being connected to the target in a certain minimum number of connections."""
    axis_values = []
    for path_group in paths.values():
        axis_values.append(len(path_group))
    return axis_values


def hovertext_formatter(paths: dict[int, list[list[str]]]) -> list[str]:
    """Returns list containing hovertext values for the bar graph. This hovertext
    represents the names of the articles that were able to be connected in a certain
    bar's minimum required number of connections.
    """
    hovertext_values = []
    for path_group in paths.values():
        hovertext_string = ''
        for path in path_group:
            if path != []:
                hovertext_string += (path[0] + '<br>')
        hovertext_values.append(hovertext_string)
    return hovertext_values


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'max-nested-blocks': 4,
        'disable': ['E1136'],
        'extra-imports': ['networkx', 'plotly.graph_objs', 'graph', 'random', 'processing'],
        'allowed-io': []
    })
