from flask import Flask,render_template,redirect,url_for,request
from models.models import Maestro,db,Alumno,Asistencia
from flask_migrate import Migrate
import os 
from formularios.forms import RegistroAlumno,RegistroDocente,Entrada
from funciones.matricula import matricula
from datetime import datetime

app = Flask(__name__)

#clavesecreta
app.config['SECRET_KEY'] = 'clavesecreta'

#Configuracion db 
directorio = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'models/asistencia.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app,db)

@app.route('/',methods=['GET','POST'])
def index():
    matriculaEntrada = Entrada()
    if matriculaEntrada.validate_on_submit():
        matricula_maestro = matriculaEntrada.matricula.data
        buscar = Maestro.query.filter(Maestro.matricula == matricula_maestro).first()
        if buscar:
            alumno_grupo = Alumno.query.filter(Alumno.grupo == buscar.grupo).all()
            
            return render_template('index.html',alumno_grupo = alumno_grupo,matricula = matriculaEntrada)
    
    return render_template('index.html',matricula = matriculaEntrada)

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

@app.route('/asistencia',methods=['POST'])
def asistencia():
    fecha = datetime.now().date()
    selccionados = request.form.getlist('opciones')
    alumno_asistencia = Asistencia(fecha,selccionados,True)
    db.session.add(alumno_asistencia)
    db.session.commit()

    return redirect(url_for('index'))

    
if __name__== '__main__':
    app.run(debug=True)