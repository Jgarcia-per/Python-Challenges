from flask import Flask, render_template
from views.controller import Controller
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', nombre='Juan')

@app.route('/perros')
def listar_perros():
    perros = Controller.retornar_perros()
    return render_template('tablePerro.html', perros = perros)



    