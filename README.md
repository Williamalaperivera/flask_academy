# 🎓 Flask Academy - Sistema de Gestión de Cursos

Este es un proyecto final desarrollado con **Python** y **Flask** para la gestión de cursos académicos. La aplicación implementa un sistema **CRUD** completo y sigue una arquitectura profesional de separación de responsabilidades, ideal para entornos escalables.

---

## 🚀 Funcionalidades Principales

* **CRUD Completo:** Gestión dinámica de cursos (Crear, Leer, Actualizar y Eliminar).
* **Arquitectura por Capas:** Separación clara de la lógica de negocio en servicios, modelos y rutas.
* **Persistencia de Datos:** Integración robusta con bases de datos mediante **SQLAlchemy ORM**.
* **Formularios Seguros:** Uso de **Flask-WTF** con validaciones personalizadas y protección contra ataques CSRF.
* **Interfaz Moderna:** Diseño responsivo con soporte para modo oscuro utilizando **Bootstrap 5**.

---

## 🎬 Demo de la Aplicación

https://github.com/user-attachments/assets/c64bea9f-7c3a-42d1-8c0e-f96702f5d14a


## 🛠️ Tecnologías Utilizadas

| Componente | Tecnología |
| :--- | :--- |
| **Backend** | Python 3.x, Flask |
| **Base de Datos** | SQL (vía SQLAlchemy ORM) |
| **Frontend** | Jinja2, HTML5, CSS3, Bootstrap 5 |
| **Librerías Clave** | Flask-WTF, WTForms, Flask-SQLAlchemy |

---

## 📁 Estructura del Proyecto

Para este proyecto se utilizó una estructura organizada que facilita el mantenimiento y la escalabilidad:

* `app.py`: Punto de entrada de la aplicación y configuración de rutas.
* `models.py`: Definición de los modelos de datos (Tablas SQL).
* `forms.py`: Definición y lógica de validación de los formularios.
* `extensions.py`: Inicialización de extensiones como SQLAlchemy.
* `services/`: Directorio que contiene la lógica de negocio y consultas a la base de datos (Ej: `curso_service.py`).
* `templates/`: Vistas HTML renderizadas con el motor Jinja2.

---

## 🔧 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/flask_academy.git](https://github.com/tu-usuario/flask_academy.git)
   cd flask_academy
