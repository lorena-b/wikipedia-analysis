"""
CSC111 Final Project - Analyzing Wikipedia Connectivity to Kevin Bacon

This is the main module, it will:
    - Create the network graph
    - Perform computations on the graph
    - Produce a Dash webpage output of the visualizations

This file is Copyright (c) 2021 Lorena Buciu, Luke Kuo, Aidan Ryan, Kevin Yang
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from graph import make_graph, make_graph_csv
from visualizations import visualize_graph, smallest_path, connectivity_bar_graph

# CONSTANTS
GOAL = 'Kevin Bacon'
LIMIT = 3  # How many directly connected articles to get per goal
DEPTH = 3  # Max depth for the article connections
CSV_NAME = 'graph_data.csv'

# CREATE THE GRAPH
graph = make_graph(GOAL, LIMIT, DEPTH)
# WRITE GRAPH TO FILE
make_graph_csv(graph)

# FRONT-END
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children=f"Wikipedia Network Analysis: 6 degrees to {GOAL}",
            style={
                'fontSize': 28,
                'paddingTop': 20,
                'paddingBottom': 20,
                'paddingLeft': 20
            }),
    html.Div(
        className="row",
        children=[
            html.Div(
                className="six columns",
                children=html.Div([
                    dcc.Graph(
                        id='right-top-graph',
                        style={'width': '90vh', 'height': '80vh'},
                        figure=visualize_graph(graph, GOAL, LIMIT, DEPTH)
                    ),
                ])
            ),
            html.Div(
                className="six columns",
                children=html.Div([
                    html.Button('Update Graph', id='button', n_clicks=0),
                    dcc.Graph(
                        id='smallest-graph'
                    ),
                    dcc.Graph(
                        id='bar-graph',
                        figure=visualize_graph(graph, GOAL, LIMIT, DEPTH)
                    ),
                ], style={"maxWidth": "800px", "maxHeight": "800px", "overflow": "scroll"})
            )
        ]
    )

])


@app.callback(Output('smallest-graph', 'figure'), [Input('button', 'n_clicks')])
def update_fig(n_clicks) -> any:
    """Update the graph by selecting a new random article to show the shortest path
    """
    if n_clicks > -1:
        return smallest_path(GOAL, CSV_NAME)

    
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
        random_article = random.choice(articles)
        print('Randomly chosen article is ' + random_article)
        path = bfs_record(wiki, random_article, target, depth_cap)
        if path == []:  # this is only returned by bfs_record() if no path is found
            print('No path found between ' + random_article + ' and ' + target +
                  ' with the chosen depth cap.')
        else:
            print('A path was found between ' + random_article + ' and ' + target +
                  ' with the chosen depth cap!')
            random_visualization(wiki, path)

    # This part isn't finished yet, but it would calculate the "paths" used in bar graph
    else:  # analysis_type == 'full'
        paths = {}
        for i in range(len(articles)):
            ...
    
    
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
