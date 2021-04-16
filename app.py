"""CSC111 Winter 2021 Final Project: Data Visualization

This file contains the dash app necessary to run the webpage

This file is Copyright (c) 2021 Aidan Ryan, Lorena Buciu, Kevin Yang, Kuan-Lin Kuo.
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from graph import make_graph, make_graph_csv
from visualizations import visualize_graph, smallest_path

# CONSTANTS
LIMIT = 3  # How many directly connected articles to get per goal
DEPTH = 3  # Max depth for the article connections


def run_dash_app(file: str, depth_cap: int, target: str) -> None:
    """Run the Dash application
    """
    # CREATE THE GRAPH
    graph = make_graph(target, LIMIT, DEPTH)
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
        html.H1(children=f"Wikipedia Network Analysis: 6 degrees to {target}",
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
                            figure=visualize_graph(graph, target, LIMIT, depth_cap)
                        ),
                    ])
                ),
                html.Div(
                    className="six columns",
                    children=html.Div([
                        html.Button('Update Graph', id='button', n_clicks=0),
                        dcc.Graph(
                            id='smallest-graph',
                            style={'width': '90vh', 'height': '80vh'}
                        ),
                    ], )
                )
            ]
        )

    ])

    @app.callback(Output('smallest-graph', 'figure'), [Input('button', 'n_clicks')])
    def update_fig(n_clicks) -> any:
        """Update the graph by selecting a new random article to show the shortest path
        """
        if n_clicks > -1:
            return smallest_path(target, file)

    app.run_server(debug=True, use_reloader=False)
