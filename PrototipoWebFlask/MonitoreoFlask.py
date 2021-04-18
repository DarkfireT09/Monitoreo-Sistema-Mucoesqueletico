"""
Code of the controller for the web app.
"""

from flask import Flask, render_template, request, url_for
import sqlalchemy
import psycopg2

# Conexion con la base de datos
try:
    connection = psycopg2.connect(host='127.0.0.1', port='5432', dbname='Cornerstone',
                                user='postgres', password='1234')
    print("Conexion con la base de datos exitosa!")
except:
    print("La conexion con la base de datos ha fallado.")
    cursor.close()
    connection.close()
cursor = connection.cursor()

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5432@localhost/Cornerstone'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user_data')
def user_data():
    try:
        cursor.execute(
            """
            SELECT *FROM "Usuario"
            WHERE "Correo" = 'david.melendez@urosario.edu.co'
            """
        )
        rows = cursor.fetchall()
    except:
        print("No username Found")
    
    nombre = rows[0][1]
    apellido = rows[0][2]
    return render_template('DatosUsuario.html', NOMBRE = nombre, APELLIDO = apellido)


@app.route('/historial')
def historial():
    return render_template('Historial.html')


@app.route('/informacion')
def informacion():
    cursor.execute(
        """
        SELECT * FROM public.persons
        ORDER BY id ASC 
        """
    )
    return render_template('Informacion.html')


@app.route('/reporte_act')
def reporte_act():
    try:
        #INSERT INTO "Usuario" (Correo, Nombre, Apellido, edad, peso, estatura, contraseña)
        cursor.execute(
        """
        INSERT INTO "Genero" ("Id", "Nombre")
        VALUES (1, 'Masculino')
        """
        )
        connection.commit()
        print("Genero insertado!")
        
    except:
        print("El Genero no pudo ser insertado!")
        connection.rollback()

    
    return render_template('ReporteActividad.html')


@app.route('/reporte_cadc')
def reporte_cadc():
    return render_template('ReporteCardiaco.html')


@app.route('/reporte_ox')
def reporte_ox():
    return render_template('ReporteOxigeno.html')


if __name__ == "__main__":
    app.run(debug=True)
