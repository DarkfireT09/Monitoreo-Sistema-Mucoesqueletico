"""
Code of the controller for the web app.
"""

from flask import Flask, render_template, request, url_for
import sqlalchemy
import psycopg2
import Modules.Notifications
import time
import Modules.global_variables

# Conexion con la base de datos
try:
    connection = psycopg2.connect(host='127.0.0.1', port='5432',
                                  dbname='Cornerstone', user='postgres',
                                  password='1234')

    print("Conexion con la base de datos exitosa!")
except:
    raise NameError("La conexion con la base de datos ha fallado.")


cursor = connection.cursor()
app = Flask(__name__)


# Notifiaciones

# Asignar el numero de notifcaciones
Modules.global_variables.numero_notificaciones_actuales = \
    Modules.Notifications.get_number_of_notifications(cursor)

Modules.Notifications.manage_notifications(cursor)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user_data')
def user_data():
    try:
        cursor.execute(
            """
            SELECT * FROM "Usuario"
		    WHERE "Correo" = 'david.melendez@urosario.edu.co'
            """
        )
        rows = cursor.fetchall()
    except:
        print("No username Found")

    nombre = rows[0][1]
    apellido = rows[0][2]
    print(rows)
    return render_template('DatosUsuario.html', NOMBRE=nombre, APELLIDO=apellido)


@app.route('/historial')
def historial():
    return render_template('Historial.html')


@app.route('/informacion')
def informacion():
    return render_template('Informacion.html')


@app.route('/reporte_act')
def reporte_act():
    try:
        # INSERT INTO "Usuario" (Correo, Nombre, Apellido, edad, peso, estatura, contraseña)
        cursor.execute(
            """
        """
        )
        connection.commit()

    except:
        connection.rollback()

    return render_template('ReporteActividad.html')


@app.route('/reporte_cadc')
def reporte_cadc():

    try:
        cursor.execute(
            """
            SELECT count(*) 
                FROM "Notificaciones"
            """
        )
        rows = cursor.fetchall()
    except:
        print("No username Found")

    return render_template('ReporteCardiaco.html')


@app.route('/reporte_ox')
def reporte_ox():
    return render_template('ReporteOxigeno.html')


if __name__ == "__main__":
    app.run(debug=True)
    
