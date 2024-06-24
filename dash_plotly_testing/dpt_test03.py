import pandas as pd
import plotly.express as px

from dash import html, dash_table, dcc, Output, Input
from django_plotly_dash import DjangoDash
from os import path
from plotly.subplots import make_subplots
from math import ceil

app = DjangoDash('DPTTest03', update_title='Actualizando gráfica')

df = pd.read_csv(path.join(
    path.dirname(__file__), "datasets/apartments.csv"))
df_desc = df.describe()
estads = list(df_desc.index)
lst_desc = [
    {**{'Estadistico': estads[i]},**r}
    for i, r in enumerate(df_desc.to_dict('records'))]

app.layout = html.Div([
    html.H1('Bogota Apartments'),
    dcc.Tabs([
        dcc.Tab([
            html.Div([
                html.Div(col, className="col")
                for col in df.columns
            ], className="row row-cols-sm-6 mb-3 mt-3"),
        ], label="Columnas"),
        dcc.Tab([
            html.Div(
                dash_table.DataTable(data=lst_desc, page_size=10),
                style={'overflow-x': 'auto'}, className="mb-3 mt-3"),
        ], label="Estadisticos"),
        dcc.Tab([
            html.Div([
                html.Div([
                    html.H3("Filtros"),
                    html.P("Tipo de Propiedad"),
                    dcc.Dropdown(
                        list(df.tipo_propiedad.unique()),
                        list(df.tipo_propiedad.unique()),
                        multi=True,
                        id="filter-tipo_propiedad"),
                ], className="col"),
                html.Div([
                    html.H3("Graficar..."),
                    dcc.Checklist([{
                        'label': 'Cada "Dimensión" en una gráfica independiente',
                        'value': 'independiente'}, ], id="multi-graph"),
                    html.Hr(),
                    dcc.Checklist([
                        {'value': 'precio_venta', 'label': 'Precio de Venta'},
                        {'value': 'precio_arriendo', 'label': 'Precio de Renta'},
                        {'value': 'administracion', 'label': 'Costo de Administración'},
                        {'value': 'area', 'label': 'Area'},
                        {'value': 'habitaciones', 'label': 'Cantidad de Habitaciones'},
                        {'value': 'banos', 'label': 'Cantidad de Baños'},
                    ], id="dimensiones", value=['precio_venta']),
                ], className="col"),
            ], className="row row-cols-sm-2 mb-3 mt-3"),
            html.Div(id="multi-graph-value"),
            html.Div(id="filter-value"),
            dcc.Graph(id="graph", config= {'displaylogo': False}, figure={}),
        ], label="Gráficas"),
    ]),
])

@app.callback(
    Output(component_id='multi-graph-value', component_property='children'),
    Input(component_id='multi-graph', component_property='value'),
)
def update_multi_graph_value(require_multiple):
    return f'El valor de multi-graph es "{require_multiple}"'

@app.callback(
    Output(component_id='filter-value', component_property='children'),
    Input(component_id="filter-tipo_propiedad", component_property="value"),
    Input(component_id="dimensiones", component_property="value")
)
def update_filters_values(
    tipo_propiedad, dimensiones):
    return f"""
        El valor de tipo_propiedad es {tipo_propiedad}.
        El valor de dimensiones = {dimensiones}
    """

@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id="filter-tipo_propiedad", component_property="value"),
    Input(component_id="dimensiones", component_property="value")
)
def update_graph(
    tipo_propiedad, dimensiones):
    df_tmp = df.copy()
    if tipo_propiedad is not None and len(tipo_propiedad) > 0:
        df_tmp = df_tmp[df_tmp['tipo_propiedad'].isin(tipo_propiedad)]
    if dimensiones is None or len(dimensiones) == 0:
        return {}
    fig = px.histogram(df_tmp, x='tipo_propiedad', histfunc='count')
    print(fig)
    # fig = make_subplots(rows=ceil(len(dimensiones) / 3), cols=3)
    # if "precio_venta" in dimensiones:
    #     print(df_tmp.columns)
    #     fig.add_trace(
    #         px.histogram(
    #             df_tmp, x='precio_venta')
    #     )
    return fig
