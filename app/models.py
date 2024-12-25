from app import db

#Create a db model (table)

class Person(db.Model):
    __tablename__ = "people"

    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.Text)
    todos = db.relationship("Todos", backref="responsible", lazy=True)

    def __repr__(self):
        return f"Person with name {self.name} and age {self.age}"
    
# 1:N Relationship
class Todos(db.Model):
    __tablename__ = "todos"

    t_id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.Text, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("people.p_id"), nullable=False)

    def __repr__(self):
        return f"To do: {self.todo}"