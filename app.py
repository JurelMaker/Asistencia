from flask import Flask
from models.models import Maestro,Imparte,Materias,db,gestor
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash,check_password_hash
import os 
from flask_login import login_user, login_required,logout_user,current_user

app = Flask(__name__)

#Configuracion db 
directorio = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'models/asistencia.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app,db)



if __name__== '__main__':
    app.run(debug=True)