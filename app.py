from flask import Flask,render_template,redirect,url_for
from models.models import Maestro,db,Alumno
from flask_migrate import Migrate
import os 
from formularios.forms import RegistroAlumno,RegistroDocente
from funciones.matricula import matricula

app = Flask(__name__)

#clavesecreta
app.config['SECRET_KEY'] = 'clavesecreta'

#Configuracion db 
directorio = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'models/asistencia.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app,db)

@app.route('/')
def index():
    pass

@app.route('/maestro',methods=['GET','POST'])
def registro_maestro():
    maestro = RegistroDocente()
    if maestro.validate_on_submit():
        maestro_nuevo = Maestro(matricula=matricula(),nombre=maestro.nombre.data,ape_pa=maestro.ape_pa.data,
                              ape_ma=maestro.ape_ma.data,fecha_nacimiento=maestro.fecha.data,grupo=maestro.grupo.data)
        db.session.add(maestro_nuevo)
        db.session.commit()

        return redirect(url_for('registro_maestro'))
    
    lista_maestro = Maestro.query.all()



    return render_template('registro_maestro.html',maestro = maestro,lista_maestro = lista_maestro)

@app.route('/alumno',methods=['GET','POST'])
def registro_alumno():
    alumno = RegistroAlumno()
    if alumno.validate_on_submit():
        alumno_nuevo = Alumno(matricula=matricula(),nombre=alumno.nombre.data,ape_pa=alumno.ape_pa.data,
                              ape_ma=alumno.ape_ma.data,fecha_nacimiento=alumno.fecha.data,grupo=alumno.grupo.data)
        db.session.add(alumno_nuevo)
        db.session.commit()

        return redirect(url_for('registro_alumno'))
    
    lista_alumnos = Alumno.query.all()
    

    return render_template('registro_alumno.html',alumno = alumno,lista_alumnos = lista_alumnos)

if __name__== '__main__':
    app.run(debug=True)