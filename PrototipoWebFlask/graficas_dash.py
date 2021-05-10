# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:37:55 2021

@author: Ana María
"""
#importar librerías para las gráficas

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import consultas as sql

#conexión con la base de datos

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#------------------RESUMEN DE LOS DATOS-------------------------

# Promedio pulso cardiaco
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.avg_pulso(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["promedio_pulso"])

# Promedio actividad física
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.avg_actividad(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["promedio_actividad"])

#Último pulso cardiaco registrado
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.ultimo_pulso(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["ultimo_pulso"])

#Último nivel de actividad física registrado
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.ultima_actividad(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["ultima_actividad"])

#Cantidad de alertas
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.avg_actividad(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["numero_alertas"])

#-------------------------REPORTES HISTÓRICOS---------------------------

#Ritmo cardiaco
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.reporte_pulso(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["fecha","pulso"])

# Grafico línea
fig_ritmo = px.line(dfCases.head(25), x="fecha", y="pulso", title='Reporte Ritmo Cardiado')

#Actividad física
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.reporte_actividad(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["fecha","actividad"])

# Grafico línea
fig_actividad = px.line(dfCases.head(25), x="fecha", y="actividad", title='Reporte Actividad Física')


# Layout 
app.layout = html.Div(children=[
    html.H1(children='REPORTES HISTÓRICOS'),
    dcc.Graph(
        id='reporteritmo',
        figure= fig_ritmo
    ),
    dcc.Graph(
        id='reporteact',
        figure= fig_actividad
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)

