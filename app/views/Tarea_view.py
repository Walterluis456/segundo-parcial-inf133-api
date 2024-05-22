from flask import render_template
from flask_login import current_user


# La función `list_animals` recibe una lista de
# animales y renderiza el template `animales.html`
def list_tareas(tareas):
    return render_template(
        "tareas.html",
        tareas=tareas,
        title="Lista de tareas",
        current_user=current_user,
    )


# La función `create_tareas` renderiza el
# template `create_tareas.html` o devuelve un JSON
# según la solicitud
def create_tareas():
    return render_template(
        "create_tareas.html", title="Crear Tarea", current_user=current_user
    )


# La función `update_tareas` recibe un tareas
# y renderiza el template `update_tareas.html`
def update_tareas(tareas):
    return render_template(
        "update_tareas.html",
        title="Editar Tarea",
        tareas=tareas,
        current_user=current_user,
    )
