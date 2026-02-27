from models import Curso
from extensions import db


def obtener_todos():
    """Retorna todos los cursos ordenados por id_curso de forma descendente."""
    return Curso.query.order_by(Curso.id_curso.desc()).all()


def agregar_curso(nombre, instructor, duracion):
    """Crea un nuevo curso y lo guarda en la base de datos."""
    nuevo_curso = Curso(
        curso=nombre,
        instructor=instructor,
        duracion=duracion
    )
    db.session.add(nuevo_curso)
    db.session.commit()


def obtener_por_id(id_curso):
    """Busca y retorna un curso por su ID. Si no existe, retorna 404 automáticamente."""
    return db.get_or_404(Curso, id_curso)


def editar_curso(id_curso, nombre, instructor, duracion):
    """Actualiza los datos de un curso existente."""
    curso = obtener_por_id(id_curso)
    curso.curso      = nombre
    curso.instructor = instructor
    curso.duracion   = duracion
    db.session.commit()


def eliminar_curso(id_curso):
    """Elimina un curso de la base de datos por su ID."""
    curso = obtener_por_id(id_curso)
    db.session.delete(curso)
    db.session.commit()