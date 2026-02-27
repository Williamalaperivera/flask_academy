from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class CursoForm(FlaskForm):
    curso = StringField(
        'Nombre del Curso',
        validators=[
            DataRequired(message='El nombre del curso es obligatorio.'),
            Length(max=150, message='El nombre no puede superar los 150 caracteres.')
        ]
    )
    instructor = StringField(
        'Instructor',
        validators=[
            DataRequired(message='El instructor es obligatorio.'),
            Length(max=100, message='El nombre del instructor no puede superar los 100 caracteres.')
        ]
    )
    duracion = DecimalField(
        'Duración (horas)',
        validators=[
            DataRequired(message='La duración es obligatoria.'),
            NumberRange(min=0.5, max=999.99, message='La duración debe estar entre 0.5 y 999.99 horas.')
        ],
        places=2
    )
    submit = SubmitField('Guardar Curso')