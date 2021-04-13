"""
Code of the controller for the web app.
"""

from flask import Flask, render_template, request, url_for
import sqlalchemy

app = Flask(__name__)

# conectar con una base de datos SQL -- Revisar como conectar con Postgres PROBLEMA

"""
app.config['SQLALCHEMY_DATABASE_URI'] = ['sqlite:///']
db = SQAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id


"""


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user_data')
def user_data():
    return render_template('DatosUsuario.html')


@app.route('/historial')
def historial():
    return render_template('Historial.html')


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
