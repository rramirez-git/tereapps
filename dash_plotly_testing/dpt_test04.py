import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from datetime import datetime
from dash import html, dash_table, dcc, Output, Input
from django_plotly_dash import DjangoDash
from plotly.subplots import make_subplots
from os import path

app = DjangoDash('DPTTest04', update_title='Actualizando gráfica')

def mes_name(mes):
    mes = int(mes)
    if mes == 1:
        return "Enero"
    if mes == 2:
        return "Febrero"
    if mes == 3:
        return "Marzo"
    if mes == 4:
        return "Abril"
    if mes == 5:
        return "Mayo"
    if mes == 6:
        return "Junio"
    if mes == 7:
        return "Julio"
    if mes == 8:
        return "Agosto"
    if mes == 9:
        return "Septiembre"
    if mes == 10:
        return "Octubre"
    if mes == 11:
        return "Noviembre"
    if mes == 12:
        return "Diciembre"

df = pd.read_csv(path.join(
    path.dirname(__file__), "datasets/DailyDelhiClimate.csv"))
df['date'] = df.date.apply(lambda date: datetime.strptime(date, '%Y-%m-%d'))
df['periodo'] = df.date.apply(lambda date: int(date.strftime('%Y%m')))
df['periodo_name'] = df.date.apply(lambda date: f"{mes_name(date.month)}, {date.year}")
df_desc = df.describe()
estads = list(df_desc.index)
lst_desc = [
    {**{'Estadistico': estads[i]},**r}
    for i, r in enumerate(df_desc.to_dict('records'))]
dims=  {
    'meantemp': 'Temperatura Media',
    'humidity': 'Húmedad',
    'wind_speed': 'Veliocidad del Viento',
    'meanpressure': 'Presión Atmosférica Media',
}

app.layout = html.Div([
    html.H1('Daily Climate time series data'),
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
                    html.P("Período"),
                    dcc.Dropdown(
                        list(df.periodo_name.unique()),
                        multi=True, id="filter-periodo"),
                ], className="col"),
                html.Div([
                    html.H3("Graficar..."),
                    dcc.Checklist([{
                        'label': 'Cada "Dimensión" en una gráfica independiente',
                        'value': 'independiente'}, ], id="multi-graph"),
                    html.Hr(),
                    dcc.Checklist([
                        {'value': k, 'label': v}
                        for k, v in dims.items()
                    ], value=[list(dims.items())[0][0], ], id="dimensiones"),
                ], className="col"),
            ], className="row row-cols-sm-2 mb-3 mt-3"),
            dcc.Graph(id="graph", config= {'displaylogo': False}, figure={}),
        ], label="Gráficas"),
    ]),
])

@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id="filter-periodo", component_property="value"),
    Input(component_id="multi-graph", component_property="value"),
    Input(component_id="dimensiones", component_property="value")
)
def update_graph(periodo, multi_graph, dimensiones):
    df_tmp = df.copy()
    if dimensiones is None or len(dimensiones) == 0:
        return {}
    if periodo is not None and len(periodo) > 0:
        df_tmp = df_tmp[df_tmp['periodo_name'].isin(periodo)]
    if multi_graph and len(multi_graph) > 0 and "independiente" in multi_graph:
        cols = 2
        dims_amt = len(dimensiones)- 1
        rows = int((dims_amt - dims_amt % 2) / 2 + 1)
        fig = make_subplots(
            cols=cols, rows=rows,
            subplot_titles=[dims[dim] for dim in dimensiones])
        for idx, dim in enumerate(dimensiones):
            fig.add_trace(
                go.Scatter(
                    x=df_tmp['date'], y=df_tmp[dim],
                    mode='lines', name=dims[dim]),
                row=int((idx - idx % 2) / 2 + 1) , col=idx % 2 + 1)
    else:
        fig = go.Figure()
        for idx, dim in enumerate(dimensiones):
            fig.add_trace(
                go.Scatter(
                    x=df_tmp['date'], y=df_tmp[dim],
                    mode='lines', name=dims[dim]))
    return fig
