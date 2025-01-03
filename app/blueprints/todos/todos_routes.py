from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
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

@todos.route("/<int:p_id>/add", methods = ["POST"])
def add_todo(p_id):
    #Get person and the new todo
    person = Person.query.get_or_404(p_id)
    form_todo = request.form.get("new_todo")

    if not form_todo in [None, ""]:
        #Create todo
        new_todo = Todos(todo=form_todo, person_id = p_id)

        #Add todo and commit changes
        person.todos.append(new_todo)
        db.session.commit()
    else:
        flash("Enter a valid to-do")

    #Redirect to get_todos()
    return redirect(url_for("todos.get_todos", id = p_id))

@todos.route("/<int:p_id>/update/<int:t_id>", methods = ["POST"])
def update_todo(p_id, t_id):
    #Get old todo and new_todo
    old_todo = Todos.query.get_or_404(t_id)
    new_todo = request.form.get("new_todo")

    #Update old todo and commit
    old_todo.todo = new_todo
    db.session.commit()

    #Redirect to get_todos()
    return redirect(url_for("todos.get_todos", id = p_id))

@todos.route("/<int:p_id>/delete/<int:t_id>", methods = ["GET"])
def delete_todo(p_id, t_id):
    #Get person and todo
    person = Person.query.get_or_404(p_id)
    todo = Todos.query.get_or_404(t_id)
    
    #Remove todo and commit
    person.todos.remove(todo)
    db.session.commit()

    #Redirect to get_todos()
    return redirect(url_for("todos.get_todos", id = p_id))
