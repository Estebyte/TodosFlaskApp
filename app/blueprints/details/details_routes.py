from flask import Blueprint, request, render_template, url_for, redirect
from models import Person
from extensions import db
from flask_login import login_required

details = Blueprint("details", __name__, url_prefix="/details", template_folder="templates")

@details.route("/<int:id>", methods = ["GET", "POST"])
@login_required
def show_details(id):
    #Get person
    person = Person.query.get_or_404(id)

    #Get values
    values = {
        column.name: getattr(person, column.name) 
        if getattr(person, column.name) not in ["", None] else "No available"
        for column in Person.__table__.columns 
        if not column.primary_key
        }

    if request.method == "GET":
        context = {
            "person" : person,
            "values" : values
        }
        return render_template("details.html", **context)
    
    #For updating the user
    elif request.method == "POST":
        #Get the values from the form
        name = request.form.get("name")
        age = int(request.form.get("age"))
        job = request.form.get("job")

        #Update the values
        person.name = name
        person.age = age
        person.job = job

        #Commit changes in the db
        db.session.commit()

        # #Return template
        # context = {
        #     "person" : person,
        #     "values" : values
        # }
        # return render_template("details.html", **context)
        return redirect(url_for("details.show_details", id = person.p_id))
    
@details.route("/<int:id>/delete")
@login_required
def delete_person(id):
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for("index"))