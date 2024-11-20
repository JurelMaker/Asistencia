from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alumno(db.Model):
    __tablename__='Alumno'
    matricula = db.Column(db.String(8),primary_key=True)
    nombre = db.Column(db.Text)
    ape_pa = db.Column(db.Text)
    ape_ma = db.Column(db.Text)
    fecha_nacimiento = db.Column(db.Date)
    grupo = db.Column(db.String(2))
    asistencia = db.relationship('Asistencia',backref='asistencias',lazy='dynamic')

    def __init__(self,matricula,nombre,ape_pa,ape_ma,fecha_nacimiento, grupo):
        self.matricula = matricula
        self.nombre = nombre
        self.ape_pa = ape_pa
        self.ape_ma = ape_ma
        self.fecha_nacimiento = fecha_nacimiento
        self.grupo = grupo


class Maestro(db.Model):
    __tablename__='Maestro'
    matricula = db.Column(db.String(8),primary_key=True)
    nombre = db.Column(db.Text)
    ape_pa = db.Column(db.Text)
    ape_ma = db.Column(db.Text)
    fecha_nacimiento = db.Column(db.Date)
    grupo = db.Column(db.String(2))
    
    def __init__(self,matricula,nombre,ape_pa,ape_ma,fecha_nacimiento,grupo):
        self.matricula = matricula
        self.nombre = nombre
        self.ape_pa = ape_pa
        self.ape_ma = ape_ma
        self.fecha_nacimiento = fecha_nacimiento
        self.grupo = grupo

class Asistencia(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fecha = db.Column(db.Date)
    idalumno = db.Column(db.String(8),db.ForeignKey('Alumno.matricula'),name='asitencia')
    asistencia = db.Column(db.Boolean)

    def __init__(self,fecha,idalumno,asistencia):
       self.fecha = fecha
       self.idalumno = idalumno
       self.asistencia = asistencia



