from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin

gestor = LoginManager()
db = SQLAlchemy()

@gestor.user_loader
def load_user(matricula):
    return Maestro.query.get(matricula)

class Alumno(db.Model):
    __tablename__='Alumno'
    matricula = db.Column(db.String(8),primary_key=True)
    nombre = db.Column(db.Text)
    ape_pa = db.Column(db.Text)
    ape_ma = db.Column(db.Text)
    fecha_nacimiento = db.Column(db.Date)

    def __init__(self,matricula,nombre,ape_pa,ape_ma,fecha_nacimiento):
        self.matricula = matricula
        self.nombre = nombre
        self.ape_pa = ape_pa
        self.ape_ma = ape_ma
        self.fecha_nacimiento = fecha_nacimiento

class Maestro(db.Model):
    __tablename__='Maestro'
    matricula = db.Column(db.String(8),primary_key=True)
    nombre = db.Column(db.Text)
    ape_pa = db.Column(db.Text)
    ape_ma = db.Column(db.Text)
    fecha_nacimiento = db.Column(db.Date)
    password = db.Column(db.String(16))
    imparte = db.relationship('Imparte',backref='mmaestro',lazy='dynamic')
    
    def __init__(self,matricula,nombre,ape_pa,ape_ma,fecha_nacimiento):
        self.matricula = matricula
        self.nombre = nombre
        self.ape_pa = ape_pa
        self.ape_ma = ape_ma
        self.fecha_nacimiento = fecha_nacimiento

    def verificar_clave(self,password):
        return check_password_hash(self.password,password)
    
    def get_id(self):
        return self.matricula

class Materias(db.Model):
    __tablename__='Materias'
    codigo = db.Column(db.String(8),primary_key=True)
    nombre = db.Column(db.Text)
    imparte = db.relationship('Imparte',backref='materias',lazy='dynamic')

    def __init__(self,nombre):
        self.nombre = nombre

class Imparte(db.Model):
    __tablename__='Imparte'
    id = db.Column(db.Integer,primary_key=True)
    id_maestro = db.Column(db.String(8),db.ForeignKey('Maestro.matricula'))
    id_materia = db.Column(db.String(8),db.ForeignKey('Materias.codigo'))

    def __init__(self,id_maestro,id_materia):
        self.id_maestro = id_maestro
        self.id_materia = id_materia
        
