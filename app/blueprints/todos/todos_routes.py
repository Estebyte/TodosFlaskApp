from flask import Blueprint, render_template
from models import Person, Todos

todos = Blueprint("todos", __name__, url_prefix="/todos", template_folder="templates")

@todos.route("/<int:id>")
def get_todos(id):
    person = Person.query.get_or_404(id)
    todos = person.todos        
    context = {
        "person" : person,
        "todos" : todos
        }
    return render_template("todos.html", **context)

@todos.route("/add", methods = ["GET", "POST"])
def add_todo():
    return ""

@todos.route("/update", methods = ["GET", "POST"])
def update_todo():
    return ""

@todos.route("/delete", methods = ["GET", "POST"])
def delete_todo():
    return ""