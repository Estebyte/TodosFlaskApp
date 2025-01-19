from extensions import db
from flask_login import UserMixin

class Person(db.Model):
    __tablename__ = "people"

    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.Text)
    todos = db.relationship("Todos", backref="responsible", lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f"Person with name {self.name} and age {self.age}"
    
class Todos(db.Model):
    __tablename__ = "todos"

    t_id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.Text, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("people.p_id"), nullable=False)

    def __repr__(self):
        return f"To do: {self.todo}"

#Users will admin the people and their to-dos    
class User(db.Model, UserMixin):
    __tablename__ = "users"

    u_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User: {self.username} Role: {self.role}"
    
    #Create a method to allow to flask_login to access to the user id
    def get_id(self):
        return self.u_id