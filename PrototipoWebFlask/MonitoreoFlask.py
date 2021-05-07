
from flask import Flask, render_template, request, url_for, jsonify
import sqlalchemy
import psycopg2
import Modules.Notifications
import datetime
import Modules.global_variables

# Conexion con la base de datos
try:
    connection = psycopg2.connect(host='127.0.0.1', port='5432',
                                  dbname='Cornerstone', user='postgres',
                                  password='1234')

    print("Conexion con la base de datos exitosa!")
except:
    raise NameError("La conexion con la base de datos ha fallado.")

# Conexion con la base de datos
try:
    notification_connection = psycopg2.connect(host='127.0.0.1', port='5432',
                                  dbname='Cornerstone', user='postgres',
                                  password='1234')

    print("Conexion con la base de datos exitosa!")
except:
    raise NameError("La conexion con la base de datos ha fallado.")


cursor = connection.cursor()
notification_cursor = notification_connection.cursor()
app = Flask(__name__)

# try:
#     cursor.execute(
#         """
#         INSERT INTO notificaciones (fecha, mensaje, correo_usuario)
#         VALUES (now()::timestamp, 'Prueba 2', 'david.melendez@urosario.edu.co')
#         """
#     )
#     connection.commit()
# except Exception as e:
#     connection.rollback()
#     print("No username Found")

try:
    cursor.execute(
        """
        SELECT nombre, apellido FROM usuario
        WHERE correo = 'david.melendez@urosario.edu.co'
        """
    )
    rows = cursor.fetchall()
    nombre = rows[0][0]
    apellido = rows[0][1]
except Exception as e:
    connection.rollback()
    print("No username Found")


# Notificaciones

# Asignar el numero de notifcaciones
Modules.global_variables.numero_notificaciones_actuales = \
    Modules.Notifications.get_number_of_notifications(notification_connection.cursor())

Modules.Notifications.manage_notifications(notification_cursor)




@app.route('/')
def index():
    return render_template('index.html', NOMBRE=nombre, APELLIDO=apellido)


@app.route('/user_data')
def user_data():
    return render_template('DatosUsuario.html', NOMBRE=nombre, APELLIDO=apellido) #Modificar DatosUsuario
                                                                            #para agregar Nombre y apellido


# @app.route('/historial')
# def historial():
#     return render_template('Historial.html')


@app.route('/Informacion')
def informacion():
    return render_template('Informacion.html')


@app.route('/ReporteActividad')
def reporte_act():
    return render_template('ReporteActividad.html')


@app.route('/ReporteCardiaco')
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

    return render_template('pulso_oxigeno.html')

@app.route('/graphics')
def graphic():
    return render_template('line-chart.js')

@app.route('/notification.js')
def notific():
    return render_template('notification.js')

# @app.route('/update_notification', methods=['POST'])
# def data_notific():
#     data = request.get_json()
#     return jsonify(data)

@app.route('/update_data', methods=['POST'])
def update_notif():
    try:
        cursor.execute(
            """
            SELECT pulso, fecha
            FROM pulsometro
            ORDER BY fecha desc
            """
        )
        rows = cursor.fetchall()
    except:
        print("No data found")

        pulso = rows[0][0]
        fecha = rows[0][1]
        return jsonify({
            'pulso': pulso,
            'fecha': fecha.strftime("%A:%H:%M:%S")
        })


if __name__ == "__main__":
    app.run(debug=True)
    pass

