from database import db


# Define la clase `Animal` que hereda de `db.Model`
# `Animal` representa la tabla `animals` en la base de datos
class Tareas(db.Model):
    __tablename__ = "tareas"

    # Define las columnas de la tabla `animals`
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(100), nullable=False)
    assigned_to = db.Column(db.String(100), nullable=False)

    # Inicializa la clase `Tareas`
    def __init__(self, id, title, description, status, created_at, assigned_to):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at
        self.assigned_to = assigned_to

    # Guarda un Tareas en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los animales de la base de datos
    @staticmethod
    def get_all():
        return Tareas.query.all()

    # Obtiene una Tarea por su ID
    @staticmethod
    def get_by_id(id):
        return Tareas.query.get(id)

    # Actualiza un Tarea en la base de datos
    def update(self, id=None, title=None, descripton=None, status= None, created_at=None, assigned_to=None):
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if descripton is not None:
            self.description = descripton
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if assigned_to is not None:
            self.assigned_to = assigned_to    
        db.session.commit()

    # Elimina una tarea de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
