"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from Connection import Connection
import consultas as sql
from datetime import datetime, timedelta

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#--------------------DATOS DE USUARIO---------------------------

con = Connection()
con.openConnection()
consulta = sql.datos_usuario() #Consulta para crear tabla de datos del usuario
cursor = con.connection.cursor()
cursor.execute(consulta)
user_data =cursor.fetchall()
fila2 = []
for i in user_data[0]:
    fila2.append(i)
con.closeConnection()
fila1=["Nombre","Apellido","Edad","Peso","Estatura", "Genero", "Ritmo Basal", "Ritmo de Reserva"]
   
#Tabla
tabla_usuario = go.Figure(data=[go.Table(header=dict(values=['Datos', 'Datos del Usuario'],
                                                     font_size=16,
                                                     height=30),
                                         cells=dict(values=[fila1, fila2],
                                                    font_size=16,
                                                    height=30))
                                ])


#------------------RESUMEN DE LOS DATOS-------------------------

# Promedio pulso cardiaco
con = Connection()
con.openConnection()
consulta = sql.avg_pulso() 
cursor = con.connection.cursor()
cursor.execute(consulta)
avg_pulso = cursor.fetchall()
con.closeConnection()


# Promedio actividad física
con = Connection()
con.openConnection()
consulta = sql.avg_actividad() 
cursor = con.connection.cursor()
cursor.execute(consulta)
avg_actividad =cursor.fetchall()
con.closeConnection()

#Último pulso cardiaco registrado
con = Connection()
con.openConnection()
consulta = sql.ultimo_pulso() 
cursor = con.connection.cursor()
cursor.execute(consulta)
ultimo_pulso =cursor.fetchall()
con.closeConnection()

#Último nivel de actividad física registrado
con = Connection()
con.openConnection()
consulta = sql.ultima_actividad() 
cursor = con.connection.cursor()
cursor.execute(consulta)
ultima_actividad =cursor.fetchall()
con.closeConnection()

#Cantidad de alertas
con = Connection()
con.openConnection()
consulta = sql.num_alertas() 
cursor = con.connection.cursor()
cursor.execute(consulta)
num_alertas =cursor.fetchall()
con.closeConnection()

#-------------------------REPORTES HISTÓRICOS---------------------------

#Ritmo cardiaco
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.reporte_pulso(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["fecha","pulso"])

# Grafico línea
fig_ritmo = px.line(dfCases.head(25), x="fecha", y="pulso")

#Actividad física
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.reporte_actividad(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["fecha","actividad"])

# Grafico línea
fig_actividad = px.line(dfCases.head(25), x="fecha", y="actividad")

#Reporte de alertas

con = Connection()
con.openConnection()
cursor = con.connection.cursor()

def get_number_of_notifications_given_day(cursor, user, timestamp) -> int:
    """
    Obtiene el numero de notificaciones (numero de filas) en la tabla 
    'notificaciones' en un dia especifico dado un usuario
    Input:
        cursor (psycopg2.connect.cursor()): cursor conectado a la base de datos
        user (str): correo del usuario
        timestamp
    Output:
        numero_de_notificaciones (int): numero de notificaciones/filas 
                                        en la tabla
    """

    try:
        sql_sentence = """
            SELECT count(*) 
            FROM Notificaciones
            WHERE correo_usuario = '{}' AND fecha > '{} 0:0:0' AND fecha < '{} 23:59:59'
            """.format(user, timestamp, timestamp)
        cursor.execute(sql_sentence)
        rows = cursor.fetchall()
    except:
        raise NameError(
            "El numero de notificaciones de un usuario no pudo ser extraido")

    numero_de_notificaciones = rows[0][0]
    return numero_de_notificaciones

dias = []
notifs = []
for i in range (0,5):
    dia = datetime.date(datetime.now() - timedelta(i))
    dias.append(dia)
    num_not = get_number_of_notifications_given_day(cursor,"ejemplo@ejemplo.com",dia)
    notifs.append(num_not)
    
fig_alertas = go.Figure(data=[go.Scatter(x=dias, y=notifs)])

# the style arguments for the upperbar

UPPERBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": "16rem",
    "right": 0,
    "height": "5rem",
    "padding": "1rem 1rem",
    "background-color": "#002233",
    "color": "white",
    'textAlign': 'center'
}

upperbar = html.Div([html.H1("NOMBRE DEL PROYECTO")],
                    style = UPPERBAR_STYLE)

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    'textAlign': 'center'
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "margin-top":"4rem",
    'textAlign': 'center'
}

BOX1_STYLE = {
    "position": "fixed",
    "top": "13rem",
    "left": "24rem",
    "width": "16rem",
    "height": "10rem",
    "background-color":"#9900cc",
    'textAlign': 'center',
    "padding": "0.5rem 0.5rem",
}

BOX2_STYLE = {
    "position": "fixed",
    "top": "13rem",
    "left": "42rem",
    "width": "16rem",
    "height":"10rem",
    "background-color":"#009933",
    "padding": "0.5rem 0.5rem",
}

BOX3_STYLE = {
    "position": "fixed",
    "top": "13rem",
    "left": "60rem",
    "width": "16rem",
    "height":"10rem",
    "background-color":"#ff9900",
    "padding": "0.5rem 0.5rem",
}

BOX4_STYLE = {
    "position": "fixed",
    "top": "24rem",
    "left": "32rem",
    "width": "16rem",
    "height":"10rem",
    "background-color":"#3399ff",
    "padding": "0.5rem 0.5rem"
}

BOX5_STYLE = {
    "position": "fixed",
    "top": "24rem",
    "left": "50rem",
    "width": "16rem",
    "height":"10rem",
    "background-color":"#ff6666",
    "padding": "0.5rem 0.5rem"
}

sidebar = html.Div(
    [
        html.H3("Menú principal"),
        html.Hr(),
        html.P(
            str("Usuario: " + user_data[0][0] + " " + user_data[0][1]), className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Resumen de los Datos", href="/", active="exact"),
                dbc.NavLink("Datos de Usuario", href="/user_data", active="exact"),
                dbc.NavLink("Reporte de Actividad", href="/reporte_act", active="exact"),
                dbc.NavLink("Reporte de Pulso Cardiaco", href="/reporte_rit", active="exact"),
                dbc.NavLink("Reporte de Alertas", href="/alertas", active="exact"),
                dbc.NavLink("Información sobre el Proyecto", href="/info", active="exact"),
                #dbc.NavLink("Guía de Uso", href="/guia", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

box1 = html.Div(children=[
    html.H3("Promedio de Pulso Cardiaco Registrado"),
    html.H4(str(int(avg_pulso[0][0]))+" bpm"),
    ],
    style= BOX1_STYLE
    )

box2 = html.Div(children=[
    html.H3("Promedio de Actividad Física Registrada"),
    html.H4(str(int(avg_actividad[0][0]))+"%"),
    ],
    style= BOX2_STYLE
    )

box3 = html.Div(children=[
    html.H3("Último Ritmo Cardiaco Registrado"),
    html.H4(str(int(ultimo_pulso[0][0]))+" bpm"),
    ],
    style= BOX3_STYLE
    )

box4 = html.Div(children=[
    html.H3("Último nivel de Actividad Física Registrado"),
    html.H4(str(int(ultima_actividad[0][0]))+" %"),
    ],
    style= BOX4_STYLE
    )

box5 = html.Div(children=[
    html.H3("Número de Alertas Totales Registradas"),
    html.H4(str(int(num_alertas[0][0]))+" alertas"),
    ],
    style= BOX5_STYLE
    )

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, upperbar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    
    #Página de Inicio: Resumen de los Datos
    if pathname == "/": 
        return html.Div(children=[
                html.H1("¡Bienvenido de nuevo!"),
                html.H2("Resumen de tu monitoreo"),
                box1,box2,box3,box4,box5
                ])
    
    #Página de reporte del ritmo cardiaco
    elif pathname == "/reporte_rit":
        return html.Div(children=[
                html.H1(children='Reporte Ritmo Cardiaco'),
                dcc.Graph(
                    id='reporteritmo',
                    figure= fig_ritmo
                    ),
                ])
    
    #Página de reporte de la actividad física
    elif pathname == "/reporte_act":
        return html.Div(children=[
                html.H1(children='Reporte Niveles de Actividad Física'),
                dcc.Graph(
                    id='reporteactividad',
                    figure= fig_actividad
                    ),
                ])
    
    
    elif pathname == "/user_data":
        return html.Div(children=[
                html.H1("Datos del Usuario"),
                dcc.Graph(
                    id='tabla',
                    figure= tabla_usuario
                    ),
               ])
               
    elif pathname == "/info":
        return html.Div(children=[ 
                html.H1("Información sobre el proyecto"),
                html.P(""),
                html.P("Este prototipo fue desarrollado por Ana Garzón, Camilo Fernández, Daniel Leyva, Gabriela Linares, Guillermo Rivero, Santiago Linares, Winston Pernett y David Alejandro Meléndez estudiantes del pregrado de Matemáticas Aplicadas y Ciencias de la Computación en La Universidad del Rosario para la materia Proyecto Cornerstone dictada por el profesor Mario Fernando Jiménez Hernández, durante el primer semestre del año 2021.", style= {'textAlign': 'center'}),
                html.H3("Objetivos"),
                html.P("El proyecto tiene como objetivos el desarrollo un dispositivo wearable, que recolecte, procese y muestre datos al usuario sobre su estado de salud y actividades físicas en tiempo real; Esta orientado hacia personas que realicen teletrabajo, y busca una estrategia tecnológica que contribuya a la prevención de algunos padecimientos relacionados con esta actividad. Para esto, se diseñó una muñequera que alberga un dispositivo creado con Arduino Lillypad y que transfiera datos de salud al presente aplicativo, donde el usuario puede visualizar los datos recopilados y recibir alertas."),
                html.H3("Documentación"),
                html.P("Si desea acceder al código o obtener mayor información sobre el proyecto, lo invitamos a revisar nuestro repositorio en Github: https://github.com/DarkfireT09/Monitoreo-Sistema-Muscoloesqueletico"),
                ])
                
   #"""elif pathname == "/guia":
        #return html.Div(children=[
                #html.H1("Guía de Uso"),
                #html.P("Aquí insertar guía de uso del dispositivo"),
               #])"""
    
    elif pathname == "/alertas":
        
        return html.Div(children=[
                html.H1("Número de alertas de los últimos 5 días"),
                dcc.Graph(
                    id='alerts',
                    figure= fig_alertas
                    ),
            ])
    
    
    
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)

