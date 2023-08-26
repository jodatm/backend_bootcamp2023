from datetime import datetime

from config import db, ma

# Se crea el modelo con los atributos
class CheckList(db.Model):
    __tablename__ = "checklist"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))    
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    
    # Representacion como String, parecido al metodo __str__
    def __repr__(self):
        return f'<Checklist {self.title}>'

# Este esquema es usado para retornar los objetos de python como JSON
# Normalmente esto se retorna en algunos APIS
class CheckListSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CheckList
        load_instance = True
        sqla_session = db.session


check_list_schema = CheckListSchema()
many_check_list_schema = CheckListSchema(many=True)

class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50))
    order = db.Column(db.Integer)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    completed = db.Column(db.Boolean, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('checklist.id', ondelete="CASCADE"))

    def __repr__(self):
        return f'<Task {self.value}>'
    
class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True
        sqla_session = db.session
        include_fk = True


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)