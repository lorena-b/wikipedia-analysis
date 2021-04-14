"""
Main File
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from graph import make_graph
from visualizations import visualize_graph

# CONSTANTS
GOAL = 'Kevin Bacon'
LIMIT = 3  # How many directly connected articles to get per goal
DEPTH = 3  # Max depth for the article connections

# CREATE THE GRAPH
graph = make_graph(GOAL, LIMIT, DEPTH)

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
    html.H1(children="Wikipedia Network Analysis: 6 degrees to Kevin Bacon",
            style={
                'fontSize': 28,
                'paddingTop': 20,
                'paddingBottom': 20,
                'paddingLeft': 20
            }),
    html.Div(
        className="row",
        children=[
            dcc.Graph(
                id='right-top-graph',
                figure=visualize_graph(graph, GOAL, LIMIT, DEPTH)
            ),
        ]
    )

])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
