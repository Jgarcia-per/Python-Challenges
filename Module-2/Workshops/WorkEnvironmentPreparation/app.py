from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from views.controller import Controller

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Perro(db.Model):
    __tablename__ = 'perro'
    id_perro = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    raza = db.Column(db.String(45))
    edad = db.Column(db.Integer)
    peso = db.Column(db.Numeric(10, 0))
    id_guarderia = db.Column(db.Integer)
    id_cuidador = db.Column(db.Integer)

class Cuidador(db.Model):
    __tablename__ = 'cuidadores'
    id_cuidadores = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    telefono = db.Column(db.String(45))
    id_guarderia = db.Column(db.Integer)

class Guarderia(db.Model):
    __tablename__ = 'guarderias'
    id_guarderia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100))
    dirrecion= db.Column(db.String(200))
    telefono = db.Column(db.String(50))

@app.route('/')
def home():
    return render_template('index.html', nombre='Juan')

@app.route('/perros')
def listar_perros():
    perros = Controller.retornar_perros()
    return render_template('tablePerro.html', perros = perros)

@app.route('/perros/Lassie')
def consulta_lassie():
    lassie = Perro.query.filter_by(nombre='Lassie').all()
    return render_template('contulta_lassie.html', perros=lassie)

@app.route('/asignar-perros-mario')
def asignar_perros_mario():
    mario = Cuidador.query.filter(Cuidador.nombre.like('Mario%')).first()
    if mario:
        Perro.query.filter(Perro.peso < 3).update({Perro.id_cuidador: mario.id_cuidadores})
        db.session.commit()
        mensaje = f"Se asignaron los perros que pesan menos de 3 kg a Mario (ID: {mario.id_cuidadores})."
    else:
        mensaje = "No se encontró al cuidador Mario."
    
    return render_template('resultado_asignacion.html', mensaje=mensaje)

@app.route('/info-favorita')
def info_favorita():
    try:
        guarderia = Guarderia.query.filter_by(nombre='La favorita').first()
        
        if not guarderia:
            return render_template('error.html', mensaje="No se encontró la guardería 'La favorita'.")

        perros = Perro.query.filter_by(id_guarderia=guarderia.id_guarderia).all()

        cuidadores = Cuidador.query.filter_by(id_guarderia=guarderia.id_guarderia).all()

        return render_template('infoFavorita.html', guarderia=guarderia, perros=perros, cuidadores=cuidadores)
    
    except Exception as e:
        print(f"Error: {e}")
        return render_template('error.html', mensaje="Ocurrió un error al consultar la información.")

if __name__ == '__main__':
    app.run(debug=True)



    