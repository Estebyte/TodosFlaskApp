from flask import render_template, request, redirect, url_for
from models import Person

def register_routes(app, db):

    @app.route("/", methods=["GET", "POST"])
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
        
    
    @app.route("/details/<int:id>")
    def details(id):
        #Get person
        person = Person.query.get_or_404(id)

        #Get values
        values = {
            column.name: getattr(person, column.name) 
            if getattr(person, column.name) not in ["", None] else "No available"
            for column in Person.__table__.columns 
            if not column.primary_key
            }

        context = {
            "person" : person,
            "values" : values
        }
        return render_template("details.html", **context)
        
    @app.route("/details/delete/<int:id>")
    def delete(id):
        person = Person.query.get_or_404(id)
        db.session.delete(person)
        db.session.commit()
        return redirect(url_for("index"))