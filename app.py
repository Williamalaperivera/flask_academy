import os
from flask import Flask, render_template, redirect, url_for, flash
from dotenv import load_dotenv
from extensions import db, migrate
from models import Curso
from forms import CursoForm
from services.curso_service import obtener_todos, agregar_curso, obtener_por_id, editar_curso, eliminar_curso

# Carga las variables del archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de la clave secreta
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Construcción de la cadena de conexión a MySQL desde las variables del .env
DB_USER     = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST     = os.getenv('DB_HOST')
DB_PORT     = os.getenv('DB_PORT')
DB_NAME     = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Registrar extensiones con la app
db.init_app(app)
migrate.init_app(app, db)


# Ruta principal
@app.route('/')
def index():
    cursos = obtener_todos()
    return render_template('index.html', cursos=cursos)


# Ruta para agregar curso
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    form = CursoForm()
    if form.validate_on_submit():
        agregar_curso(
            nombre=form.curso.data,
            instructor=form.instructor.data,
            duracion=form.duracion.data
        )
        flash('✅ Curso agregado exitosamente.', 'success')
        return redirect(url_for('index'))
    return render_template('agregar_curso.html', form=form)


# Ruta para editar curso
@app.route('/editar/<int:id_curso>', methods=['GET', 'POST'])
def editar(id_curso):
    curso = obtener_por_id(id_curso)
    form = CursoForm(obj=curso)
    if form.validate_on_submit():
        editar_curso(
            id_curso=id_curso,
            nombre=form.curso.data,
            instructor=form.instructor.data,
            duracion=form.duracion.data
        )
        flash('✏️ Curso actualizado exitosamente.', 'success')
        return redirect(url_for('index'))
    return render_template('editar_curso.html', form=form, curso=curso)


# Ruta para eliminar curso
@app.route('/eliminar/<int:id_curso>', methods=['POST'])
def eliminar(id_curso):
    eliminar_curso(id_curso)
    flash('🗑️ Curso eliminado exitosamente.', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)