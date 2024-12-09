from flask import render_template, request
from models import Person

def register_routes(app, db):

    @app.route("/")
    def index():
        #Query all in person table
        people = Person.query.all()
        context = {
            "people" : people
        }
        return render_template("index.html", **context)
