from flask import render_template, request, redirect, url_for
from models import Person
from flask_login import login_required

def register_routes(app, db, bcrypt):

    @app.route("/", methods=["GET", "POST"])
    @login_required
    def index():
        if request.method == "GET":
            #Query all in person table
            people = Person.query.all()
            context = {
                "people" : people
            }
            return render_template("index.html", **context)
        
        elif request.method == "POST":
            #Get the values from the form
            name = request.form.get("name")
            age = int(request.form.get("age"))
            job = request.form.get("job")

            #Create a person object with the values of the form
            person = Person(name=name, age=age, job=job)

            #Add the person to the db and commit the changes
            db.session.add(person)
            db.session.commit()

            #Query all in person table
            people = Person.query.all()
            context = {
                "people" : people
            }
            return render_template("index.html", **context)