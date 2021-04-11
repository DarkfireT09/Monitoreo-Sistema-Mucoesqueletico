# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

#conectar con una base de datos SQL -- Revisar como conectar con Postgres
 
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///']
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

if __name__ == "__main__":
    app.run(debug=True)
