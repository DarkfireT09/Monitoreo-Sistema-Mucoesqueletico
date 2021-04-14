"""
Code of the controller for the web app.
"""

from flask import Flask, render_template, request, url_for
import sqlalchemy
import psycopg2

# Conexion con la base de datos
try:
    conexion = psycopg2.connect(host='127.0.0.1', port='5432', dbname='Cornerstone',
                                user='postgres', password='1234')
    print("Conexion con la base de datos exitosa!")
except:
    print("La conexion con la base de datos ha fallado.")
    cursor.close()
    conexion.close()
cursor = conexion.cursor()

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5432@localhost/Cornerstone'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user_data')
def user_data():
    cursor.execute(
        """
        SELECT * FROM public.persons
        ORDER BY id ASC 
        """
    )
    rows = cursor.fetchall()
    for row in rows:
        print("Yahoo: ", row)
    return render_template('DatosUsuario.html')


@app.route('/historial')
def historial():
    return render_template('Historial.html')


@app.route('/informacion')
def informacion():
    return render_template('Informacion.html')


@app.route('/reporte_act')
def reporte_act():
    return render_template('ReporteActividad.html')


@app.route('/reporte_cadc')
def reporte_cadc():
    return render_template('ReporteCardiaco.html')


@app.route('/reporte_ox')
def reporte_ox():
    return render_template('ReporteOxigeno.html')


if __name__ == "__main__":
    app.run(debug=True)
