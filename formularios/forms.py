from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class RegistroAlumno(FlaskForm):    
    nombre = StringField('Nombre',validators=[DataRequired()]
                        ,render_kw={"type": "text"})
    
    ape_pa = StringField('Apellido Paterno',validators=[DataRequired()],render_kw={"type": "text"})

    ape_ma = StringField('Apellido Materno',validators=[DataRequired()],render_kw={"type": "text"})

    fecha = DateField('Fecha',format='%Y-%m-%d',validators=[DataRequired()],
                      render_kw={"type": "date"})
    
    grupo = SelectField('Grupo', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], validators=[DataRequired()])

    boton = SubmitField('Registrar',render_kw={"class":"submit-btn"})

class RegistroDocente(FlaskForm):    
    nombre = StringField('Nombre',validators=[DataRequired()]
                        ,render_kw={"type": "text"})
    
    ape_pa = StringField('Apellido Paterno',validators=[DataRequired()],render_kw={"type": "text"})

    ape_ma = StringField('Apellido Materno',validators=[DataRequired()],render_kw={"type": "text"})

    fecha =  DateField('Fecha',format='%Y-%m-%d',validators=[DataRequired()],
                      render_kw={"type": "date"})
    
    grupo = SelectField('Grupo', choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], validators=[DataRequired()])
    
    boton = SubmitField('Registrar',render_kw={"class":"submit-btn"})

class Entrada(FlaskForm):
    matricula = StringField('Nombre',validators=[DataRequired()]
                        ,render_kw={"type": "text"})

    boton = SubmitField('Registrar',render_kw={"class":"submit-btn"})

class Enviar(FlaskForm):
    enviar = SubmitField('Enviar',render_kw={"class":"submit-btn"})