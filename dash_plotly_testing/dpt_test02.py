import pandas as pd
import plotly.express as px

from dash import Input
from dash import Output
from dash import dash_table
from dash import dcc
from dash import html
from django_plotly_dash import DjangoDash

app = DjangoDash('DPTTest02')

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminder2007.csv')

app.layout = html.Div([
    html.H1(children='My First App with Data, Graph, and Controls'),
    html.Div(
        className='row',
        children=[
            html.Div(className='col-sm-6', children=[
                dash_table.DataTable(
                    data=df.to_dict('records'), page_size=10),
                ]),
            html.Div(className='col-sm-6', children=[
                dcc.Graph(figure=px.histogram(
                    df, x='continent', y='lifeExp', histfunc='avg')),
                ]),
        ]),
    html.Div(className='row', children=[
        html.Div(className='col-sm-3 text-right', children=[
            dcc.RadioItems(
                options=['pop', 'lifeExp', 'gdpPercap'],
                value='lifeExp', id='controls-and-radio-item'),
        ]),
        html.Div(className='col-sm-9', children=[
            dcc.Graph(
                figure={}, id='controls-and-graph',
                config={'displaylogo': False}),
        ]),
    ]),
])


@app.callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig
